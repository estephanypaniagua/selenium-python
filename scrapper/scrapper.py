from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .utils.tools import wait_for_text, wait_for_class, wait_for_element, fill_text_input, pick_select_input, mark_checkbox_input
from .utils.generator import ItemInfo, ShippingInfo, Order


def go_to_login_page(driver: webdriver) -> None:
    # Find login button and click
    login_button_selector = "#app > div > div.header.flex.justify-between > div.icon-wrapper.flex.justify-between.space-x-1 > div:nth-child(2) > a"
    login_button_selector = '//*[@id="app"]/div/div[1]/div[3]/div[2]/a'
    login_button = driver.find_element(By.XPATH, login_button_selector)
    login_button.click()

    # Wait for login to load after click
    form_id = "loginForm"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, form_id)))


def sign_in(driver: webdriver, email: str, password: str) -> None:
    # Find login form elements
    email_input_selector = '//*[@id="loginForm"]/div[1]/div[1]/input'
    pass_input_selector = '//*[@id="loginForm"]/div[2]/div[1]/input'
    sign_in_button_selector = '//*[@id="loginForm"]/div[3]/button'
    email_input = driver.find_element(By.XPATH, email_input_selector)
    pass_input = driver.find_element(By.XPATH, pass_input_selector)
    sign_in_button = driver.find_element(By.XPATH, sign_in_button_selector)

    # Fill in login form and submit
    email_input.send_keys(email)
    pass_input.send_keys(password)
    sign_in_button.click()


def sign_up(driver: webdriver, name: str, email: str, password: str) -> None:
    # Go to sign up page
    create_account_link_selector = '//*[@id="app"]/div/main/div/div/div/a'
    create_account_link = driver.find_element(
        By.XPATH, create_account_link_selector)
    create_account_link.click()

    # Wait for "Create A New Account" text to load
    title_selector = '//*[@id="app"]/div/main/div/div/h1'
    title_text = 'Create A New Account'
    WebDriverWait(driver, 10).until(wait_for_text(title_selector, title_text))

    # Find login form elements
    full_name_input_selector = '//*[@id="loginForm"]/div[1]/div/input'
    email_input_selector = '//*[@id="loginForm"]/div[2]/div/input'
    pass_input_selector = '//*[@id="loginForm"]/div[3]/div/input'
    sign_up_button_selector = '//*[@id="loginForm"]/div[4]/button'
    full_name_input = driver.find_element(By.XPATH, full_name_input_selector)
    email_input = driver.find_element(By.XPATH, email_input_selector)
    pass_input = driver.find_element(By.XPATH, pass_input_selector)
    sign_up_button = driver.find_element(By.XPATH, sign_up_button_selector)

    # Fill in login form and submit
    full_name_input.send_keys(name)
    email_input.send_keys(email)
    pass_input.send_keys(password)
    sign_up_button.click()


def go_to_shopping_page(driver: webdriver) -> None:
    # Find shopping button and click
    shop_now_button_selector = '//*[@id="app"]/div/main/div[1]/div/div[2]/a'
    shop_now_button = driver.find_element(By.XPATH, shop_now_button_selector)
    shop_now_button.click()

    # Wait for shopping to load after click
    shopping_heading_selector = '//*[@id="app"]/div/main/div[1]/div/div/h1'
    shopping_heading_text = 'WOMEN'
    WebDriverWait(driver, 10).until(wait_for_text(
        shopping_heading_selector, shopping_heading_text))


def get_item_selector(item_number: int) -> str:
    # item1_selector = '//*[@id="app"]/div/main/div[2]/div[2]/div[2]/div/div[1]/div[2]/a'
    # item2_selector = '//*[@id="app"]/div/main/div[2]/div[2]/div[2]/div/div[2]/div[2]/a'
    return f'//*[@id="app"]/div/main/div[2]/div[2]/div[2]/div/div[{item_number}]/div[2]/a'


def add_item_to_cart(driver: webdriver, item_number: int, qty: int) -> ItemInfo:
    # Click in item
    item_selector = get_item_selector(item_number)
    item = driver.find_element(By.XPATH, item_selector)
    item_name = item.text
    item.click()

    # Wait for item to load after click
    item_heading_selector = '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[1]/h1'
    WebDriverWait(driver, 10).until(
        wait_for_text(item_heading_selector, item_name))

    item_size_button_selector = '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]/a'
    item_size_button_box_selector = '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[2]/div[1]/ul/li[1]'
    item_size_button = driver.find_element(By.XPATH, item_size_button_selector)
    item_size_button.click()
    WebDriverWait(driver, 10).until(wait_for_class(
        item_size_button_box_selector, "selected"))

    item_color_button_selector = '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]/a'
    item_color_button_box_selector = '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[2]/div[2]/ul/li[1]'
    item_color_button = driver.find_element(
        By.XPATH, item_color_button_selector)
    item_color_button.click()
    WebDriverWait(driver, 10).until(wait_for_class(
        item_color_button_box_selector, "selected"))

    item_qty_input_selector = '//*[@id="productForm"]/div/div/div[1]/div/div/input'
    item_qty_input = driver.find_element(By.XPATH, item_qty_input_selector)
    item_qty_input.clear()
    item_qty_input.send_keys(str(qty))

    add_to_cart_button_selector = '//*[@id="productForm"]/div/div/div[2]/button'
    add_to_cart_button = driver.find_element(
        By.XPATH, add_to_cart_button_selector)
    add_to_cart_button.click()

    return ItemInfo(name=item_name, qty=qty)


def go_back_to_shopping_page(driver: webdriver):
    continue_shopping_link_selector = '//*[text()="Continue shopping"]'
    WebDriverWait(driver, 10).until(
        wait_for_element(continue_shopping_link_selector))
    continue_shopping_link = driver.find_element(
        By.XPATH, continue_shopping_link_selector)
    continue_shopping_link.click()

    women_heading_link_selector = '//*[@id="app"]/div/div[1]/div[2]/ul/li[3]/a'
    women_heading_link = driver.find_element(
        By.XPATH, women_heading_link_selector
    )
    women_heading_link.click()


def add_items_to_cart(driver: webdriver, qty: int) -> list[ItemInfo]:
    items_list: list[ItemInfo] = []
    for i in range(1, qty + 1):
        new_item = add_item_to_cart(driver, item_number=i, qty=randint(1, 4))
        items_list.append(new_item)
        go_back_to_shopping_page(driver)

    return items_list


def go_to_checkout_page(driver: webdriver):
    cart_link_selector = '//*[@id="app"]/div/div[1]/div[3]/div[1]/a'
    cart_link = driver.find_element(By.XPATH, cart_link_selector)
    cart_link.click()

    checkout_button_selector = '//*[@id="app"]/div/main/div/div/div[2]/div/div[2]/div/div[2]/a'
    WebDriverWait(driver, 10).until(wait_for_element(checkout_button_selector))
    checkout_button = driver.find_element(
        By.XPATH, checkout_button_selector)
    checkout_button.click()

    sleep(10)

    continue_to_payment_button_selector = '//*[@id="checkoutShippingAddressForm"]/*/button'
    WebDriverWait(driver, 10).until(
        wait_for_element(continue_to_payment_button_selector))


def fill_checkout_page(driver: webdriver, shipping_info: ShippingInfo):
    fill_text_input(driver,
                    '//input[@name="address[full_name]"]', shipping_info.full_name)
    fill_text_input(driver,
                    '//input[@name="address[telephone]"]', shipping_info.telephone)
    fill_text_input(driver,
                    '//input[@name="address[address_1]"]', shipping_info.address)
    fill_text_input(driver,
                    '//input[@name="address[city]"]', shipping_info.city)
    pick_select_input(driver,
                      '//select[@name="address[country]"]')
    pick_select_input(driver,
                      '//select[@name="address[province]"]')
    fill_text_input(driver,
                    '//input[@name="address[postcode]"]', shipping_info.postcode)
    sleep(2)

    mark_checkbox_input(driver,
                        '//label[@for="method0"]')

    sleep(1)

    continue_to_payment_button_selector = '//*[@id="checkoutShippingAddressForm"]/div[2]/button'
    continue_to_payment_button = driver.find_element(
        By.XPATH, continue_to_payment_button_selector)
    continue_to_payment_button.click()


def fill_payment_page(driver: webdriver):
    sleep(2)
    card_checkbox_selector = '//*[@id="checkoutPaymentForm"]/div[2]/div[3]/div/div/div/div[1]/a'
    WebDriverWait(driver, 10).until(wait_for_element(card_checkbox_selector))
    card_checkbox = driver.find_element(By.XPATH, card_checkbox_selector)
    card_checkbox.click()

    test_success_button_selector = '//*[@id="checkoutPaymentForm"]/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/button[1]'
    test_success_button = driver.find_element(
        By.XPATH, test_success_button_selector)
    test_success_button.click()

    sleep(2)

    test_card_number_selector = '//*[@id="checkoutPaymentForm"]/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]'
    test_card_expiry_selector = '//*[@id="checkoutPaymentForm"]/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[3]'
    test_card_cvc_selector = '//*[@id="checkoutPaymentForm"]/div[2]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[4]'

    test_card_number_fulltext = driver.find_element(
        By.XPATH, test_card_number_selector).text
    test_card_expiry_fulltext = driver.find_element(
        By.XPATH, test_card_expiry_selector).text
    test_card_cvc_fulltext = driver.find_element(
        By.XPATH, test_card_cvc_selector).text

    test_card_number = test_card_number_fulltext.split(': ')[-1]
    test_card_expiry = test_card_expiry_fulltext.split(': ')[-1]
    test_card_cvc = test_card_cvc_fulltext.split(': ')[-1]

    iframe_selector = '//div[@id="card-element"]/div/iframe'
    iframe_selector = '//*[@id="card-element"]/div/iframe'
    iframe = driver.find_element(By.XPATH, iframe_selector)
    driver.switch_to.frame(iframe)

    card_number_input = driver.find_element(
        By.XPATH, '//input[@name="cardnumber"]')
    card_expiry_input = driver.find_element(
        By.XPATH, '//input[@name="exp-date"]')
    card_cvc_input = driver.find_element(
        By.XPATH, '//input[@name="cvc"]')

    card_number_input.send_keys(test_card_number)
    card_expiry_input.send_keys(test_card_expiry)
    card_cvc_input.send_keys(test_card_cvc)

    driver.switch_to.default_content()

    place_order_button_selector = '//*[@id="checkoutPaymentForm"]/div[3]/button'
    place_order_button = driver.find_element(
        By.XPATH, place_order_button_selector)

    place_order_button.click()


def validate_order(driver: webdriver, number_of_items: int) -> Order:
    order_success_selector = '//*[@id="app"]/div/main/div/div[1]/div/h3'
    WebDriverWait(driver, 10).until(wait_for_element(order_success_selector))

    contact_information_email = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]').text

    shipping_full_name = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]').text
    shipping_address = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]').text
    shipping_postcode_city = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[1]').text
    shipping_postcode, shipping_city = [
        x.strip() for x in shipping_postcode_city.split(',')]

    shipping_province_country = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]').text
    shipping_province, shipping_country = [
        x.strip() for x in shipping_province_country.split(',')]

    shipping_phone = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[4]').text

    items_info: list[ItemInfo] = []
    for i in range(1, number_of_items + 1):
        item_name = driver.find_element(
            By.XPATH, f'//*[@id="summary-items"]/table/tbody/tr[{i}]/td[2]/div/div[1]/span').text
        item_qty = driver.find_element(
            By.XPATH, f'//*[@id="summary-items"]/table/tbody/tr[{i}]/td[1]/div/span').text
        item_subtotal = driver.find_element(
            By.XPATH, f'//*[@id="summary-items"]/table/tbody/tr[{i}]/td[3]/span').text
        items_info.append(ItemInfo(item_name, int(item_qty), item_subtotal))

    order_qty_raw = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]').text
    order_qty = int(order_qty_raw.split(' ')[0])
    order_total = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/main/div/div[2]/div/div[2]/div[4]/div/div[2]').text

    return Order(
        email=contact_information_email,
        shipping_info=ShippingInfo(
            full_name=shipping_full_name,
            address=shipping_address,
            postcode=shipping_postcode,
            city=shipping_city,
            telephone=shipping_phone,
            # province=shipping_province,
            # country=shipping_country,
        ),
        items_info=items_info,
        qty=order_qty,
        total=order_total,
    )
