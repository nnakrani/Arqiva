import requests
from utils.logger import logger

def test_api_health_check():
    logger.info("Starting API health check test.")
    response = requests.get("https://www.arqiva.com")
    
    if response.status_code == 200:
        logger.info("API health check passed.")
    else:
        logger.error(f"API health check failed with status code {response.status_code}.")
    
    assert response.status_code == 200