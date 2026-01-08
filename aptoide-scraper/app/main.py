#imports da FastAPI e funções criadas
from fastapi import FastAPI, HTTPException, Query
from app.scraper import AptoideScraper
from app.schemas import AppResponse
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Aptoid Scraper API",
    description="API para scraping de dados de apps do Aptoide",
    version="1.0.0"
)

@app.get("/aptoide", response_model=AppResponse)
async def get_aptoide_app(
    package_name: str = Query(
        ...,
        title="Package Name",
        description = "Nome do pacote do app (ex: com.facebook.katana)",
        example = "com.facebook.katana"
    )
):

    scraper = AptoideScraper()

    try:
        app_data = await scraper.get_app_data(package_name)
        return app_data

    except AppNotFoundError:
        raise HTTPException(
            status_code = 404,
            detail=f"App com package '{package_name}' não encontrado no Aptoidde"
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Erro interno: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Erro interno ao processar requisição"
        )

@app.get("/health")
async def health_check():
    #Endpoint de saúde da API
    return{"status": "healthy", "service": "aptoide-scraper"}
