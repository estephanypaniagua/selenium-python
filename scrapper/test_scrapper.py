from time import sleep

from .scrapper import go_to_login_page, sign_up, sign_in, go_to_shopping_page, add_items_to_cart, go_to_checkout_page, fill_checkout_page, fill_payment_page, validate_order
from .utils.driver import get_chrome_driver
from .utils.generator import get_customer_info, get_shipping_info


def test_scrapper():
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

    order = validate_order(driver, number_of_items=len(items_info_list))

    assert order.email == customer_info.email
    assert order.shipping_info.full_name == shipping_info.full_name
    assert order.shipping_info.address == shipping_info.address
    assert order.shipping_info.city == shipping_info.city
    assert order.shipping_info.state == shipping_info.state
    assert order.shipping_info.zip_code == shipping_info.zip_code
    assert order.shipping_info.country == shipping_info.country
    assert order.shipping_info.phone == shipping_info.phone

    for item_original, item_result in zip(items_info_list, order.items_info):
        assert item_original.name == item_result.name
        assert item_original.quantity == item_result.quantity

    driver.quit()
