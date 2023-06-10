import pytest
from solutions.CHK import checkout_solution

DISCOUNTS = [
    checkout_solution.Discount(
        required_items=checkout_solution.Basket().create_basket("AAA"),
        removed_items=checkout_solution.Basket().create_basket("AAA"),
        discount_value=checkout_solution.Items.A.value.total_price*3-130
    ),
    checkout_solution.Discount(
        required_items=checkout_solution.Basket().create_basket("AAAAA"),
        removed_items=checkout_solution.Basket().create_basket("AAAAA"),
        discount_value=checkout_solution.Items.A.value.total_price*5-200
    ),
    checkout_solution.Discount(
        required_items=checkout_solution.Basket().create_basket("BB"),
        removed_items=checkout_solution.Basket().create_basket("BB"),
        discount_value=checkout_solution.Items.B.value.total_price*2-45
    ),
    checkout_solution.Discount(
        required_items=checkout_solution.Basket().create_basket("EE"),
        removed_items=checkout_solution.Basket().create_basket("EEB"),
        discount_value=checkout_solution.Items.B.value.total_price
    )
]

@pytest.fixture
def greeting_template():
    return "Hello, {}!"


@pytest.fixture
def discount_table():
    return DISCOUNTS
