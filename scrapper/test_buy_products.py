from time import sleep

from .scrapper import go_to_login_page, sign_up, sign_in, go_to_shopping_page, add_items_to_cart, go_to_checkout_page, fill_checkout_page, fill_payment_page, validate_order
from .utils.driver import get_chrome_driver
from .utils.generator import get_customer_info, get_shipping_info

# This test is going to sign up a new user, add items to cart, fill the checkout page and validate the order.
def test_buy_products():
    home_page = "https://demo.evershop.io"
    driver = get_chrome_driver()
    driver.get(home_page)

    customer_info = get_customer_info()
    print(customer_info)
    shipping_info = get_shipping_info()
    print(shipping_info)

    go_to_login_page(driver)
    driver.save_screenshot('./screenshots/login.png')
    sign_up(driver,
            customer_info.name, customer_info.email, customer_info.password)
    driver.save_screenshot('./screenshots/sign_up.png')

    sleep(2)

    go_to_shopping_page(driver)
    driver.save_screenshot('./screenshots/shopping.png')
    items_info_list = add_items_to_cart(driver, 3)
    print(items_info_list)

    go_to_checkout_page(driver)
    driver.save_screenshot('./screenshots/go_to_checkout.png')
    fill_checkout_page(driver, shipping_info)
    driver.save_screenshot('./screenshots/fill_checkout.png')
    fill_payment_page(driver)
    driver.save_screenshot('./screenshots/payment.png')

    sleep(2)

    order = validate_order(driver, number_of_items=len(items_info_list))

    assert order.email == customer_info.email
    assert order.shipping_info.full_name == shipping_info.full_name
    assert order.shipping_info.telephone == shipping_info.telephone
    assert order.shipping_info.address == shipping_info.address
    assert order.shipping_info.city == shipping_info.city
    assert order.shipping_info.postcode == shipping_info.postcode

    items_original = sorted(items_info_list, key=lambda item: item.name)
    items_returned = sorted(order.items_info, key=lambda item: item.name)

    for item_original, item_result in zip(items_original, items_returned):
        assert item_original.name == item_result.name
        assert item_original.qty == item_result.qty

    driver.quit()
