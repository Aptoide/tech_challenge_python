import httpx
import asyncio
from bs4 import BeautifulSoup
import re

async def debug():
    url = "https://facebook.en.aptoide.com/app"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        print("DEBUG DO HTML")

        # Verifica título
        title = soup.find('title')
        print(f"1. Titulo encontrado: {title.text if title else 'NÃO'}")

        # Procura os downloads
        print("\n2. Buscando 'downloads' no HTML: ")

        # Tudo encontrado como "download"
        all_texts = soup.find_all(text=re.compile(r'download', re.IGNORECASE))
        for i, text in enumerate(all_texts[:10]):
            print(f"    [{i}] Texto: {text.strip()[:100]}...")
            print(f"    Parent: {text.parent.name if text.parent else 'None'}")
            print(f"    Classes: {text.parent.get('class') if text.parent else 'None'}")
        
        # Procura por "APK Information"
        print("\n3. Buscando 'APK Information':")
        apk_sections = soup.find_all(text=re.compile(r'APK Information', re.IGNORECASE))
        for i, text in enumerate(apk_sections):
            print(f"    [{i}] Encontrado: {text.strip()}")
            print(f"    Parent: {text.parent if text.parent else 'None'}")
            if text.parent:
                print(f"    HTML próximo: {str(text.parent)[:200]}...")
        
        # Salva HTML para analisar
        with open('debug_facebook.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f"\nHTML salvo em 'debug_facebook.html'")

        # Procura números
        print("\n4. Buscando números que podem ser downloads ou versão:")
        numbers = soup.find_all(text=re.compile(r'\d+[BMK]?\+|\d+\.\d+\.\d+'))
        for i, num in enumerate(numbers[:15]):
            print(f"    [{i}] Número encontrado: {num.strip() if num.strip() else 'VAZIO'}")

asyncio.run(debug())