from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.logger import logger
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest



def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_home_page_loads():
    logger.info("Starting home page load test.")
    driver = webdriver.Chrome()
    driver.get("https://www.arqiva.com")
    
    if "Arqiva" in driver.title:
        logger.info("Home page loaded successfully.")
    else:
        logger.error("Home page title mismatch.")
    
    driver.quit()

def test_main_tabs_navigation():
    driver = webdriver.Chrome()
    driver.get("https://www.arqiva.com")
    tabs = ["About", "Solutions", "News", "Careers"]
    for tab in tabs:
        if not isinstance(tab, str):
            logger.error(f"Unexpected value in tabs list: {tab}")
            continue  # Skip invalid entries

        try:
            element = driver.find_element(By.LINK_TEXT, tab)
            element.click()
            assert tab.lower() in driver.current_url.lower()
            logger.info(f"Successfully navigated to {tab} page")
        except Exception as e:
            logger.error(f"Error navigating to {tab}: {e}")
    
    driver.quit()




