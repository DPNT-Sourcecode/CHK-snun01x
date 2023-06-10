# noinspection PyUnusedLocal
# skus = unicode string
import collections
import dataclasses
import re
from typing import Dict


def validate_skus(skus):
    """Ensure skus are a valid string [A-Z]
    Parameters
    ----------
    skus

    Returns
    -------

    """
    pattern = "^[A-Z]+$"
    if not re.fullmatch(pattern, skus):
        raise TypeError(f"Expected {skus} to match {pattern}")


def combine_skus_duplicates(skus: str) -> Dict[str, int]:
    """
    Counts the frequency of each SKU in a given string.

    The function takes a string of SKUs where each SKU is represented by
    an uppercase letter [A-Z]. It returns a dictionary where the keys are
    the SKUs and the values are the count of each SKU in the input string.

    Parameters
    ----------
    skus : str
        A string containing the SKUs to be counted. Each SKU should be an uppercase
        letter [A-Z].

    Returns
    -------
    dict
        A dictionary where the keys are the unique SKUs from the input string and the
        values are the count of each SKU.
        If a SKU is not present in the input string, it will not appear in the output
        dictionary.

    Examples
    --------
    >>> combine_skus_duplicates('AAB')
    {'A': 2, 'B': 1}

    >>> combine_skus_duplicates('ABC')
    {'A': 1, 'B': 1, 'C': 1}
    """
    combined = collections.defaultdict(int)
    for sku in skus:
        combined[sku] += 1
    return combined


@dataclasses.dataclass
class Discount:
    price: int
    discount_value: int = 0
    discount_meet_quantity: int = 1

    def apply_discount(self, num_items: int):
        total_discounts = num_items % self.discount_meet_quantity
        remainder = num_items // self.discount_meet_quantity
        return total_discounts * self.discount_value + remainder * self.price


DISCOUNT_TABLE = {
    'A': Discount(price=50, discount_value=130, discount_meet_quantity=3),
    'B': Discount(price=30, discount_value=45, discount_meet_quantity=2),
    'C': Discount(price=20),
    'D': Discount(price=15),
}


def apply_dicount(n: int, dicount: Discount):
    """

    Parameters
    ----------
    n
    k: divisor

    Returns
    -------
    n % k, n // k
    """
    return, n // k


def compute_sku_counts_with_discounts(sku_counts: Dict[str, int]) -> int:
    return {get_modulo_remainder(n, q_to_meet_discount) for n, q_to_meet_discount in
            discounts_map.items()}


def checkout(skus):
    """

        Assumed input format:
        'ABCKIEKD' where each char is in the alphabet
        Our price table and offers:
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+

     - For any illegal input return -1
        Parameters
        ----------
        skus

        Returns
        -------
        int: total checkout value
    """
    validate_skus(skus)
    combined = combine_skus_duplicates(skus)
    # discounts
    raise NotImplementedError()

