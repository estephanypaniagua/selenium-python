from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException


def text_to_be_present_in_element(locator, text_):
    """An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """

    def _predicate(driver: webdriver):
        try:
            element_text = driver.find_element(*locator).text.lower()
            return text_.lower() in element_text
        except StaleElementReferenceException:
            return False

    return _predicate


def class_to_be_present_in_element(locator, css_class: str):
    """An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """

    def _predicate(driver: webdriver):
        try:
            element = driver.find_element(*locator)
            return css_class in element.get_attribute('class')
        except StaleElementReferenceException:
            return False

    return _predicate


def wait_for_text(xpath: str, text: str) -> str:
    return text_to_be_present_in_element((By.XPATH, xpath), text)


def wait_for_class(xpath: str, css_class: str) -> str:
    return class_to_be_present_in_element((By.XPATH, xpath), css_class)


def wait_for_element(xpath: str) -> str:
    return EC.visibility_of_element_located((By.XPATH, xpath))


def fill_text_input(driver: webdriver, xpath: str, text: str) -> None:
    input = driver.find_element(By.XPATH, xpath)
    input.send_keys(text)


def pick_select_input(driver: webdriver, xpath: str) -> None:
    select = Select(driver.find_element(By.XPATH, xpath))
    select.options[1].click()


def mark_checkbox_input(driver: webdriver, xpath: str) -> None:
    checkbox = driver.find_element(By.XPATH, xpath)
    checkbox.click()
