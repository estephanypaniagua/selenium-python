from time import sleep

from .scrapper import go_to_login_page, sign_up, sign_in, go_to_shopping_page, add_items_to_cart, go_to_checkout_page, fill_checkout_page, fill_payment_page, validate_order
from .utils.driver import get_chrome_driver
from .utils.generator import get_customer_info, get_shipping_info


def main():
    home_page = "https://demo.evershop.io"
    driver = get_chrome_driver()
    driver.get(home_page)

    customer = get_customer_info()
    print(customer)
    shipping_info = get_shipping_info()
    print(shipping_info)

    go_to_login_page(driver)
    sign_up(driver, customer.name, customer.email, customer.password)
    # sign_in(driver, "xrobinson@example.net", "63$ImmTc&K")

    sleep(2)

    go_to_shopping_page(driver)
    add_items_to_cart(driver, 2)

    go_to_checkout_page(driver)
    fill_checkout_page(driver, shipping_info)
    fill_payment_page(driver)

    sleep(2)

    validate_order(driver)

    driver.close()
