import pytest
from solutions.CHK import checkout_solution

from ..conftest import DISCOUNTS


def _get_sku_parametrization():
    return (
        "skus,expected",
        [
            ("A", checkout_solution.Items.A.value.total_price),
        ],
    )

class TestItem:

    def test_item_initialization(self):
        item = checkout_solution.Item('A', 50, 3)
        assert item.key == 'A'
        assert item.price == 50
        assert item.quantity == 3

    def test_item_total_price(self):
        item = checkout_solution.Item('A', 50, 3)
        assert item.total_price == 150

    def test_item_construct(self):
        item = checkout_solution.Item('A', 50)
        assert item.quantity == 1
        item.construct(3)
        assert item.quantity == 3
        assert item.total_price == 150

class TestBasket:

    def test_basket_initialization(self):
        basket = checkout_solution.Basket()
        assert isinstance(basket.items, dict)
        assert basket.value == 0

    def test_basket_create(self):
        basket = checkout_solution.Basket()
        basket.create_basket("AAABBB")
        assert len(basket.items) == 2
        assert basket.items["A"].quantity == 3
        assert basket.items["B"].quantity == 3

    def test_basket_value(self):
        basket = checkout_solution.Basket()
        basket.create_basket("AAABBB")
        assert basket.value == (checkout_solution.Items["A"].value.total_price*3 + checkout_solution.Items["B"].value.total_price*3)

    def test_basket_subtraction(self):
        basket1 = checkout_solution.Basket().create_basket("AAABBB")
        basket2 = checkout_solution.Basket().create_basket("AAB")
        basket1 - basket2
        assert basket1.items["A"].quantity == 1
        assert basket1.items["B"].quantity == 2

    def test_basket_subtraction_error(self):
        basket1 = checkout_solution.Basket().create_basket("AAABBB")
        basket2 = checkout_solution.Basket().create_basket("AABCC")
        with pytest.raises(TypeError):
            basket1 - basket2

class TestDiscount:

    def setup_method(self):
        self.basket = Basket().create_basket("AAABBB")
        self.discount = Discount(
            required_items=Basket().create_basket("AAA"),
            removed_items=Basket().create_basket("AAA"),
            discount_value=Items["A"].value.total_price*3 - 130
        )

    def test_discount_initialization(self):
        assert isinstance(self.discount.required_items, Basket)
        assert self.discount.discount_value == 20

    def test_discount_apply(self):
        discount_value = self.discount.apply_discount(self.basket)
        assert discount_value == 20
        assert self.basket.items["A"].quantity == 1

    def test_discount_comparison(self):
        other_discount = Discount(
            required_items=Basket().create_basket("BB"),
            removed_items=Basket().create_basket("BB"),
            discount_value=Items["B"].value.total_price*2 - 45
        )
        assert not self.discount <= other_discount
        assert other_discount <= self.discount
class TestCHK:
    @pytest.mark.parametrize(
        "input_skus",
        [
            "a",
            "1",
            "abc",
            "A B C",
            "123",
        ],
    )
    def test_validate_skus_invalid(self, input_skus):
        # ARRANGE
        # ACT
        # ASSERT
        with pytest.raises(TypeError):
            checkout_solution.validate_skus(input_skus)

    @pytest.mark.parametrize("input_skus", ["AA", "AB", ""])
    def test_validate_skus_valid(self, input_skus):
        # ARRANGE
        # ACT
        # ASSERT
        checkout_solution.validate_skus(input_skus)

    @pytest.mark.parametrize(
        "skus,expected",
        [
            ("A", {"A": 1}),
            ("AA", {"A": 2}),
            ("ABC", {"A": 1, "B": 1, "C": 1}),
            ("AAB", {"A": 2, "B": 1}),
            ("", {}),
        ],
    )
    def test_combine_skus_duplicates(self, skus, expected):
        # ARRANGE
        # ACT
        combined = checkout_solution.combine_skus_duplicates(skus)
        # ASSERT
        assert combined == expected

    @pytest.mark.parametrize(*_get_sku_parametrization())
    def test_compute_discounts(self, skus, expected):
        assert checkout_solution.compute_discounts(skus) == expected

    @pytest.mark.parametrize(*_get_sku_parametrization())
    def test_checkout(self, skus, expected):
        assert checkout_solution.checkout(skus) == expected

    def test_checkout_err(self):
        assert checkout_solution.checkout("invalid") == -1



