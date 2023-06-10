import pytest

from solutions.CHK import checkout_solution


class TestCHK:

    @pytest.mark.parametrize("input_skus", [
        'a',
        '1',
        'abc',
        'A B C',
        '123',
        '',
    ])
    def test_validate_skus_invalid(self, input_skus):
        # ARRANGE
        # ACT
        # ASSERT
        with pytest.raises(TypeError):
            checkout_solution.validate_skus(input_skus)

    @pytest.mark.parametrize("input_skus", [
        'AA',
        'AB'
    ])
    def test_validate_skus_valid(self, input_skus):
        # ARRANGE
        # ACT
        # ASSERT
        checkout_solution.validate_skus(input_skus)

    def test_checkout(self):
        pass

