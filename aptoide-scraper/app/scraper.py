import httpx
from bs4 import BeautifulSoup
from typing import Dict, Optional
import logging
import re

logger = logging.getLogger(__name__)

class AptoideScraper:
    def __init__(self):
        self.base_url = "https://{package_name}.en.aptoide.com/app"
        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )

    async def get_app_data(self, package_name: str) -> Dict[str, str]:
        base_name = self._extract_base_name(package_name)
        url = self.base_url.format(package_name = base_name)

        logger.info(f"Buscando app em: {url}")

        try:
            response = await self.client.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            #Procura por verificação
            if not self._app_exists(soup):
                raise ValueError(f"App com package '{package_name}' não foi encontrado")

            #Extrair dados
            app_data = self._extract_all_data(soup,package_name)
            return app_data

        except httpx.HTTPStatusError as e:
            logger.error (f"Erro HTTP {e.response.status_code} para {package_name}")
            if e.response.status_code == 404:
                raise ValueError (f"App '{package_name}' não encontrado")
            raise
        finally:
            await self.client.aclose()

    def _extract_base_name(self, package_name: str) -> str:
        #Extrair dados facebook de katana
        if package_name.startswith('com.'):
            parts = package_name.split('.')
            if len(parts) >= 2:
                return parts[1]
        return package_name

    def _app_exists(self, soup: BeautifulSoup) -> bool:
        #Verifica existencia do app
        title = soup.find('title')
        if title and 'APK Download' in title.text:
            return True

        apk_section = soup.find(text="APK Information")
        return apk_section is not None
    
    def _extract_all_data(self, soup: BeautifulSoup, package_name:str) -> Dict [str,str]:
        #Extrair campos da pag
        data = {}

        #Nome
        title= soup.find('title')
        if title:
            name = title.text.replace(' - APK Download for Android', '').strip()
            data['name'] = name
        
        #Downloads
        downloads_elem = soup.find(text=lambda t: t and 'downloads' in t.lower())
        if downloads_elem:
            parent = downloads_elem.parent
            if parent:
                downloads_text = parent.get_text(strip=True)
                match = re.search(r'(\d+\.?\d*[BMK]?\+?)', downloads_text)
                if match:
                    data['downloads'] = match.group(1)
        
        # Extrai da secção "APK Information"
        apk_header = soup.find(lambda tag: tag.name in ['h2', 'h3', 'h4'] and 'APK Information' in tag.text)

        if apk_header:
            container = apk_header.find_next('div') or apk_header.parent

            for item in container.find_all(['p', 'div', 'span']):
                text = item.get_text(strip=True)
                if ':' in text:
                    key, value = text.split(':', 1)
                    key = key.strip().lower()
                    value = value.strip()

                    field_map = {
                        'package': 'package_id',
                        'apk version': 'version',
                        'size': 'size',
                        'release date': 'release_date',
                        'min screen': 'min_screen',
                        'supported cpu': 'supported_cpu',
                        'sha1 signature': 'sha1_signature',
                        'developer (cn)': 'developer_cn',
                        'organization (o)': 'organization',
                        'local (l)': 'local',
                        'country (c)': 'country',
                        'state/city (st)': 'state_city'
                    }

                    if key in field_map:
                        data[field_map[key]] = value

        #Verifica package_id
        data ['package_id'] = package_name

        #Verifica a existencia de campos obrigatórios
        required_fields = [
            'name', 'size', 'downloads', 'version', 'release_date',
            'min_screen', 'supported_cpu', 'package_id', 'sha1_signature',
            'developer_cn', 'organization', 'local', 'country', 'state_city'
        ]

        for field in required_fields:
            if field not in data:
                data[field] = "Not available"
        
        return data

    #Função auxiliar
async def fetch_app_data(package_name: str) -> Dict[str, str]:
    scraper = AptoideScraper()
    return await scraper.get_app_data(package_name)