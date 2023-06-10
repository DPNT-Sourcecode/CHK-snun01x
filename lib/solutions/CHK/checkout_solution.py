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

    @property
    def total_price(self) -> int:
        return self.quantity * self.price

    def construct(self, quantity: int):
        self.quantity = quantity
        return self


class Items(Enum):
    A = Item('A', 50)
    B = Item('B', 30)
    C = Item('C', 20)
    D = Item('D', 15)
    E = Item('E', 40)


class Basket:
    _items: Dict[str, Item]

    @property
    def value(self):
        return sum([item.total_price for item in self.items.values()])

    @property
    def items(self):
        if self._items is None:
            self._items = {}
        return self._items

    def create_basket(self, skus):
        combined = combine_skus_duplicates(skus)
        for key, quantity in combined.items():
            self.items[key] = Item(key=key, quantity=quantity)


@dataclasses.dataclass
class Discount:
    discount_basket: Basket
    discount_value: int
    discount_lambda: Callable[[Basket], Basket]  # a function that applies the discount

    def __post_init__(self):
        # Calculate the value of discount on initialization
        normal_price = sum(
            item.total_price for item in self.discount_basket.items)
        self.discount_value = normal_price - self.discount_value

    def apply_discount(self, basket: Basket):
        """
        Applies the discount to the provided basket.

        Parameters
        ----------
        basket : Basket
            The basket to which the discount will be applied.

        Returns
        -------
        Basket
            The basket after applying the discount.

        Raises
        ------
        ValueError
            If the discount cannot be applied to the basket.
        """
        if self.can_apply_discount(basket):
            return self.discount_lambda(basket)
        else:
            raise ValueError("Discount cannot be applied to this basket.")

    def can_apply_discount(self, basket: Basket):
        """
        Checks if the discount can be applied to the provided basket.

        Parameters
        ----------
        basket : Basket
            The basket to which the discount will be applied.

        Returns
        -------
        bool
            True if the discount can be applied, otherwise False.
        """
        # Iterate over each item in the discount basket
        for discount_key, discount_item in self.discount_basket.items.items():
            # Try to find the corresponding item in the basket
            basket_item = basket.items.get(discount_key)
            # If the item is not found in the basket, or there are not enough of
            # them, return False
            if not basket_item or basket_item.quantity < discount_item.quantity:
                return False
        # If we've made it here, the basket meets the discount criteria


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


