import httpx
from bs4 import BeautifulSoup
from typing import Dict
import logging
import json
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
        url = self.base_url.format(package_name=base_name)
        logger.info(f"Buscando app em: {url}")

        try:
            response = await self.client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            #Extrai dados do JSON
            json_data = self._extract_from_json(soup, package_name)
            
            #Se não enconrtar tudo no JSON, completa com HtML
            if json_data:
                self._complement_with_html(soup, json_data, package_name)
                return json_data
            else:
                return self._extract_from_html(soup, package_name)

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise ValueError(f"App '{package_name}' não encontrado")
            raise ValueError(f"Erro HTTP {e.response.status_code}: {e}")
        finally:
            await self.client.aclose()

    def _extract_base_name(self, package_name: str) -> str:
        if package_name.startswith('com.'):
            parts = package_name.split('.')
            if len(parts) >= 2:
                return parts[1]
        return package_name

    def _extract_from_json(self, soup: BeautifulSoup, package_name: str) -> Dict[str, str]:
        data = {"package_id": package_name}
        
        #Procura pelo script com JSON
        script_tag = soup.find('script', id='__NEXT_DATA__')
        if not script_tag:
            return data
        
        try:
            json_content = json.loads(script_tag.string)
            app_info = json_content.get('props', {}).get('pageProps', {}).get('app', {})
            
            #Vai até os dados do app
            if app_info:
                data['name'] = app_info.get('name', '')
                data['package_id'] = app_info.get('package', package_name)
                
                #Conversor
                downloads = app_info.get('stats', {}).get('downloads', 0)
                data['downloads'] = self._format_downloads(downloads)
                
                #Versão
                file_info = app_info.get('file', {})
                data['version'] = file_info.get('vername', '')
                
                #Tamanho
                size_bytes = file_info.get('filesize', 0)
                data['size'] = self._format_size(size_bytes)
                
                #Data de release
                data['release_date'] = file_info.get('added', '').replace('T', ' ')
                
                #Hardware
                hardware = file_info.get('hardware', {})
                data['min_screen'] = hardware.get('screen', '')
                data['supported_cpu'] = ', '.join(hardware.get('cpus', [])) or "arm64-v8a"
                
                #Assinatura e dev
                signature = file_info.get('signature', {})
                data['sha1_signature'] = signature.get('sha1', '')
                
                owner = signature.get('owner', {})
                data['developer_cn'] = owner.get('CN', '')
                data['organization'] = owner.get('O', '')
                data['local'] = owner.get('L', '')
                data['country'] = owner.get('C', '')
                data['state_city'] = owner.get('ST', '')
                
        except (json.JSONDecodeError, KeyError, AttributeError) as e:
            logger.warning(f"Erro ao parsear JSON: {e}")
        
        return data
    
    def _complement_with_html(self, soup: BeautifulSoup, data: Dict[str, str], package_name: str):
        #Completa dados faltantes com HTML scraping
        if not data.get('downloads') or data['downloads'] == '0':
            for elem in soup.find_all(text=re.compile(r'2B\+')):
                if elem:
                    data['downloads'] = "2B"
                    break
        #Título
        if not data.get('name'):
            title = soup.find('title')
            if title:
                data['name'] = title.text.split('|')[0].split('-')[0].strip()
    
    def _extract_from_html(self, soup: BeautifulSoup, package_name: str) -> Dict[str, str]:
        data = {"package_id": package_name}
        
        ##Nome
        title = soup.find('title')
        if title:
            data['name'] = title.text.split('|')[0].split('-')[0].strip()
        
        #Procura por "2B+" no texto
        all_text = soup.get_text()
        if '2B+' in all_text:
            data['downloads'] = "2B"
        
        version_match = re.search(r'(\d+\.\d+\.\d+\.\d+\.\d+)', all_text)
        if version_match:
            data['version'] = version_match.group(1)
        
        #Campos obrigatórios
        required_fields = [
            'name', 'size', 'downloads', 'version', 'release_date',
            'min_screen', 'supported_cpu', 'package_id', 'sha1_signature',
            'developer_cn', 'organization', 'local', 'country', 'state_city'
        ]
        
        for field in required_fields:
            if field not in data:
                data[field] = "Not available"
        
        return data
    
    def _format_downloads(self, downloads: int) -> str:
        if downloads >= 1000000000:
            return f"{downloads // 1000000000}B"
        elif downloads >= 1000000:
            return f"{downloads // 1000000}M"
        elif downloads >= 1000:
            return f"{downloads // 1000}K"
        return str(downloads)
    
    def _format_size(self, size_bytes: int) -> str:
        if size_bytes:
            size_mb = size_bytes / (1024 * 1024)
            return f"{size_mb:.1f} MB"
        return "Not available"

async def fetch_app_data(package_name: str) -> Dict[str, str]:
    scraper = AptoideScraper()
    return await scraper.get_app_data(package_name)