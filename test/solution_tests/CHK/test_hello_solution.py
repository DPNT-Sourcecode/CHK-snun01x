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


class TestDiscount:
    @pytest.mark.parametrize(
        "num_items,expected",
        [
            (1, 10),  # price=50, discount_value=30, discount_meet_quantity=2
            (2, 15),  # 2 items hit the discount threshold
            (3, 25),  # 2 items hit the discount threshold, 1 item at regular price
            (4, 30),  # 4 items hit the discount threshold
        ],
    )
    def test_apply_discount(self, num_items, expected):
        # ARRANGE
        discount = checkout_solution.Discount(
            price=10, discount_value=15, discount_meet_quantity=2
        )

        # ACT
        total = discount.apply_discount(num_items)

        # ASSERT
        assert total == expected

    def test_apply_discount_no_discount(self):
        # ARRANGE
        price = 5
        num_items = 10
        discount = checkout_solution.Discount(price=price)

        # ACT
        total = discount.apply_discount(num_items)

        # ASSERT
        assert total == price * num_items


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

