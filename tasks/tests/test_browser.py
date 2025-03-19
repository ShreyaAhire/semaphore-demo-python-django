"""
    Unit Test file for views
"""
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pydjango_ci_integration.settings import SITE_URL

class TaskListViewTest(TestCase):
    """
    Test View class
    """
    def test_chrome_site_homepage(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-test")  # Unique user data directory

        service = Service("/usr/local/bin/chromedriver")  # Ensure correct path to chromedriver
        browser = webdriver.Chrome(service=service, options=chrome_options)
        
        browser.get(SITE_URL)
        self.assertIn("Semaphore", browser.title)
        browser.quit()  # Use quit() instead of close() to ensure full cleanup
