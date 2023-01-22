from dataclasses import dataclass
from faker import Faker
from typing import Optional


@dataclass
class CustomerInfo:
    name: str
    email: str
    password: str


@dataclass
class ItemInfo:
    name: str
    qty: int
    unit_price: Optional[int] = None
    subtotal: Optional[int] = None


@dataclass
class ShippingInfo:
    full_name: str
    telephone: str
    address: str
    city: str
    postcode: str


def get_customer_info() -> CustomerInfo:
    fake = Faker()
    return CustomerInfo(name=fake.name(), email=fake.email(), password=fake.password())


def get_shipping_info() -> ShippingInfo:
    fake = Faker()

    return ShippingInfo(
        full_name=fake.name(),
        telephone=fake.phone_number(),
        address=fake.street_address(),
        city=fake.city(),
        postcode=fake.postcode()
    )
