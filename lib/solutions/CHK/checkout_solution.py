import collections
import dataclasses
import re
from enum import Enum
from typing import Dict, Set, Callable, Tuple, List


@dataclasses.dataclass
class Item:
    key: str
    price: int
    quantity: int = None

    def construct(self, quantity: int):
        self.quantity = quantity
        return self


class Items(Enum):
    A = Item('A', 50)
    B = Item('B', 30)
    C = Item('C', 20)
    D = Item('D', 15)
    E = Item('E', 40)


@dataclasses.dataclass
class Basket:
    _items: Set[Item]

    @property
    def items(self):
        if self._items is None:
            self._items = set()
        return self._items

    def create_basket(self, skus):
        combined = combine_skus_duplicates(skus)
        for key, quantity in combined.items():
            self.items.add(Item(key=key,
                                quantity=quantity))


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

    original: Basket
    discounted: Basket

    def apply_discount(self, basket: Basket):
        """

        Parameters
        ----------
        basket

        Returns
        -------

        """


DISCOUNT_TABLE: List[Tuple[Discount, Callable[[Basket], Basket]]] = [
    Discount(
        original=Basket({Item('A').construct(3)}),
        discounted=Basket()
    )
]


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




