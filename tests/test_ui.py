from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import logger
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import sys
import os
##sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_home_page_loads():
    ##logger.info("Starting home page load test.")
    ##driver = webdriver.Chrome()
    driver.get("https://www.arqiva.com")
    
    if "Arqiva" in driver.title:
        logger.info("Home page loaded successfully.")
    else:
        logger.error("Home page title mismatch.")
    
    driver.quit()

def test_main_tabs_navigation():
    driver = webdriver.Chrome()
    driver.get("https://www.arqiva.com")
    tabs = [("About", "ABOUT"), ("Solutions", "SOLUTIONS"), ("News", "NEWS"), ("Careers", "CAREERS"), ("Error", "ERROR")] #Added an Invalid check as well
    
    for tab, text in tabs:
        driver.find_element(By.LINK_TEXT, tab).click()
        if text in driver.title.upper():
            logger.info(f"Navigation to {tab} successful.")
        else:
            logger.error(f"Navigation to {tab} failed: Expected '{text}' in title but got '{driver.title.upper()}'.")
    
    driver.quit()




