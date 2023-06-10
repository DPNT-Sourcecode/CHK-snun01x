from typing import Any


# noinspection PyShadowingBuiltins,PyUnusedLocal

def _assert_int_in_range_0_100(n: Any):
    """Check for type and range of.
    Raises TypeError ValueError
    Parameters
    ----------
    n: Any

    Returns
    -------

    """
    if not isinstance(n, int):
        raise TypeError(f'Type: {type(n)} should by of type {int}')


def compute(x: int, y: int) -> int:
    """Returns sum of two positive integers range 0 -> 100.

    In order to complete the round you need to implement the following method:
         sum(Integer, Integer) -> Integer

    Where:
     - param[0] = a positive integer between 0-100
     - param[1] = a positive integer between 0-100
     - @return = an Integer representing the sum of the two numbers

    Parameters
    ----------
    x: int 0->100
    y: int 0->100

    Returns
    -------

    """
    _assert_int_int_in_range_0_100(x)
    _assert_int_int_in_range_0_100(y)

    return x + y



