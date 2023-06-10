import collections
import dataclasses
import re
from typing import Dict


@dataclasses.dataclass
class Discount:
    """
    A data class representing a discount.

    Attributes
    ----------
    price : int
        The regular price of the item.
    discount_value : int
        The discount applied when the quantity meets the discount threshold.
    discount_meet_quantity : int
        The quantity threshold to meet for the discount to be applied.
    """

    price: int
    discount_value: int = 0
    discount_meet_quantity: int = 1
    free: list = None

    def apply_discount(self, num_items: int):
        """
        Apply the discount to a certain number of items.

        Parameters
        ----------
        num_items : int
            The number of items to apply the discount to.

        Returns
        -------
        int
            The total price after applying the discount.
        """
        # default case of no discounts provided (should just be price)
        if self.discount_meet_quantity == 1:
            return self.price * num_items
        total_discounts = num_items // self.discount_meet_quantity
        remainder = num_items % self.discount_meet_quantity
        # for default cases as n%1 = 0
        return total_discounts * self.discount_value + remainder * self.price


DISCOUNT_TABLE: Dict[str, Discount] = {
    "A": [
        Discount(price=50, discount_value=200, discount_meet_quantity=5),
        Discount(price=50, discount_value=130, discount_meet_quantity=3),
    ],
    "B": Discount(price=30, discount_value=45, discount_meet_quantity=2),
    "C": Discount(price=20),
    "D": Discount(price=15),
    "E": [
        Discount(price=30, discount_value=45, discount_meet_quantity=2, free=['B']),
    ],
}


def validate_skus(skus):
    """Ensure skus are a valid string [A-Z]
    Parameters
    ----------
    skus

    Returns
    -------

    """
    if skus == "":
        return
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


def compute_discounts(skus: str) -> int:
    """Computest the total price given the frequency of skus as a str.
    Parameters
    ----------
    skus : str
    A string containing the SKUs to be counted. Each SKU should be an uppercase
    letter [A-Z].

    Returns
    -------

    """
    combined = combine_skus_duplicates(skus)
    combined = {
        key: DISCOUNT_TABLE[key].apply_discount(val) for key, val in combined.items()
    }
    return sum(combined.values())


def checkout(skus: str) -> int:
    """Compute skus checkout value given discounts

    Parameters
    ----------
    skus: string representing skus

    Returns
    -------
    int: > 0 or -1 for error.
    """
    try:
        validate_skus(skus)
    except TypeError:
        return -1
    return compute_discounts(skus)



