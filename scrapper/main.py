from time import sleep

from .scrapper import go_to_login_page, sign_up, sign_in, go_to_shopping_page, add_items_to_cart, go_to_checkout_page, fill_checkout_page, fill_payment_page, validate_order
from .utils.driver import get_chrome_driver
from .utils.generator import get_customer_info, get_shipping_info


def main():
    home_page = "https://demo.evershop.io"
    driver = get_chrome_driver()
    driver.get(home_page)

    customer_info = get_customer_info()
    print(customer_info)
    shipping_info = get_shipping_info()
    print(shipping_info)

    go_to_login_page(driver)
    sign_up(driver,
            customer_info.name, customer_info.email, customer_info.password)
    # sign_in(driver, "xrobinson@example.net", "63$ImmTc&K")

    sleep(2)

    go_to_shopping_page(driver)
    items_info_list = add_items_to_cart(driver, 3)
    print(items_info_list)

    go_to_checkout_page(driver)
    fill_checkout_page(driver, shipping_info)
    fill_payment_page(driver)

    sleep(2)

    validate_order(driver, customer_info, shipping_info, items_info_list)

    driver.quit()
