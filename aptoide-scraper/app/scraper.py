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
            timeout= 30.0,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        )
    
    async def get_app_data(self, package_name: str) -> Dict [str,str]:
        base_name = self._extract_base_name(package_name)
        url = self.base_url.format(package_name=base_name)

        logger.info(f"Buscando app em: {url}")

        try:
            response = await self.client.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parse')

            #Extrai dados do JSON
            json_data = self._extract_from_json(soup,package_name)

            #Se não enconrtar tudo no JSON, completa com HtML
            if json_data:
                self._complement_with_html(soup, json_data, package_name)
                return json_data
            else:
                return self._extract_from_html(soup, package_name)

        except httpx.HTTPException as e:
            if e.response.status_code == 404:
                raise ValueError(f"App '{package_name}' não encontrado")
            raise
        finally:
            await self.client.aclose()

    def _extract_base_name(self, package_name: str) -> str:
        if package_name.startswith('com.'):
            parts = package_name.split('.')
            if len(parts) >= 2:
                return parts[1]
        return package_name
    
    def _exctract_from_json(self, soup: BeautifulSoup, package_name:str) -> Dict[str,str]:
        data = {"package_id": package_name}

        #Procura pelo script com JSON
        script_tag = soup.find('script', id='__NEXT_DATA__')

        if not script_tag:
            return data
        
        try:
            json_content = json.loads(script_tag.string)

            #Vai até os dados do app
            app_info = json_content.get('props', {}).get('pageProps', {}).get('app', {})

            if app_info:
                data['name'] = app_info.get('name', '')
                data['package_id'] = app_info.get('package', package_name)

                #Conversor
                downloads = app_info.get('stats', {}).get('download', 0)
            