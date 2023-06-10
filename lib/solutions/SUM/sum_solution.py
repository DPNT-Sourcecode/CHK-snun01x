from typing import Any

# noinspection PyShadowingBuiltins,PyUnusedLocal


def _assert_int_in_range_0_100(n: Any):
    """Check n is of type int and in range 0 -> 100
    Raises TypeError ValueError
    Parameters
    ----------
    n: Any

    Returns
    -------

    """
    if not isinstance(n, int):
        raise TypeError(f"Type: {type(n)} should by of type {int}")

    if not 0 <= n <= 100:
        raise ValueError(f"Integer {n} Expected to be in range of 0 <= n <= 100")


def compute(x: int, y: int) -> int:
    """Returns sum of two positive integers range 0 -> 100.

    Parameters
    ----------
    x: int 0->100
    y: int 0->100

    Returns
    -------

    """
    for v in (x, y):
        _assert_int_in_range_0_100(v)
    return x + y
