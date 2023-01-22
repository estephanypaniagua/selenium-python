from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller


def get_chrome_driver() -> webdriver:
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=[
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        "--disable-setuid-sandbox",
    ])
    return driver
