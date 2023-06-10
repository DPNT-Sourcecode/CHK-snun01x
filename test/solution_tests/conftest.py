import pytest
from solutions.CHK.checkout_solution import Discount

DISCOUNT_TABLE = {
    "A": Discount(price=50, discount_value=130, discount_meet_quantity=3),
    "B": Discount(price=30, discount_value=45, discount_meet_quantity=2),
    "C": Discount(price=20),
    "D": Discount(price=15),
}


@pytest.fixture
def greeting_template():
    return "Hello, {}!"


@pytest.fixture
def discount_table():
    return DISCOUNT_TABLE
