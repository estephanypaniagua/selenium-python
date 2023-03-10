from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_chrome_driver() -> webdriver:
    if environ.get("CI") == "true":
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(800, 800))
        display.start()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver
