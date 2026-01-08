import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.scraper import AptoideScraper

async def test():
    scraper = AptoideScraper()
    try:
        data = await scraper.get_app_data("com.facebook.katana")
        print("Funcionou!")
        for key in ['name', 'downloads', 'version', 'package_id']:
            print(f"{key}: {data.get(key, 'N/A')}")
    except Exception as e:
        print(f"Erro: {type(e).__name__}: {e}")

if __name__ == "__main__":
    asyncio.run(test())