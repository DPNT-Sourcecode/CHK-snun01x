from typing import Any, Union

import pytest

from solutions.SUM import sum_solution


class TestSum():
    @pytest.mark.parametrize(
        ('n', 'error'),
        [
            (0, None),
            (100, None),
            ('str', TypeError),
            (-100, ValueError),
        ]
    )
    def test__assert_int_in_range_0_100(self, n: Any, error: Union[None, Any]):
        if error:
            with pytest.raises(error):
                sum_solution._assert_int_in_range_0_100(n)
        sum_solution._assert_int_in_range_0_100(n)

    def test_compute(self):
        assert sum_solution.compute(1, 2) == 3

