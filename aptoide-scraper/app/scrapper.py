import httpx
from bs4 import BeaultifulSoup
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class AptoideScrapper:
    def __init__(self):
        self.base_url = "https.//{package_name}.en.aptoide.com/app"
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

            soup = BeaultifulSoup(response.text, 'html.parser')

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
