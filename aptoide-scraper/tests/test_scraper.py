import asyncio
import sys
sys.path.append('.')

from app.scraper import AptoideScraper

async def main():
    scraper = AptoideScraper()
    try:
        data = await scraper.get_app_data("com.facebook.katana")
        print("Funcionou!")
        for key, value in data.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Erro: {e}")

asyncio.run(main())