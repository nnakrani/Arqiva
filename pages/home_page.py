from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.arqiva.com"
        
        # Locators
        self.main_tabs = {
            "About": (By.LINK_TEXT, "About"),
            "Solutions": (By.LINK_TEXT, "Solutions"),
            "News": (By.LINK_TEXT, "News"),
            "Careers": (By.LINK_TEXT, "Careers"),
        }

    def open(self):
        """Navigate to the homepage."""
        self.driver.get(self.url)

    def verify_homepage_title(self):
        """Verify that the homepage title contains 'Arqiva'."""
        return "Arqiva" in self.driver.title

    def navigate_to_tab(self, tab_name):
        """Click on a main navigation tab."""
        if tab_name in self.main_tabs:
            self.driver.find_element(*self.main_tabs[tab_name]).click()
            return True
        return False