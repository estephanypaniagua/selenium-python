from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver() -> webdriver:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=[
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        "--disable-setuid-sandbox",
    ])
    return driver
