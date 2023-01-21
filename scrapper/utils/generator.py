from dataclasses import dataclass
from faker import Faker


@dataclass
class Customer:
    name: str
    email: str
    password: str


@dataclass
class ShippingInfo:
    full_name: str
    telephone: str
    address: str
    city: str
    postcode: str


def get_customer_info() -> Customer:
    fake = Faker()
    return Customer(name=fake.name(), email=fake.email(), password=fake.password())


def get_shipping_info() -> ShippingInfo:
    fake = Faker()

    return ShippingInfo(
        full_name=fake.name(),
        telephone=fake.phone_number(),
        address=fake.street_address(),
        city=fake.city(),
        postcode=fake.postcode()
    )
