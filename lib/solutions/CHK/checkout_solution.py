from __future__ import annotations
import collections
import dataclasses
import functools
import re
from enum import Enum
from typing import Dict, Set, Callable, Tuple, List


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
class Item:
    key: str
    price: int
    quantity: int = 1

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
    def items(self)-> Dict[str, Item]:
        if not hasattr(self,'_items'):
            self._items = {}
        return self._items

    def create_basket(self, skus):
        combined = combine_skus_duplicates(skus)
        for key, quantity in combined.items():
            item=Items[key].value
            self.items[key] = Item(key=key, quantity=quantity,price=item.total_price)
        return self

    def __sub__(self, other: Basket):
        """Subtracts another Basket instance from this one."""
        if not isinstance(other, Basket):
            raise TypeError(f"Unsupported operand type for -: {type(other)}")

        for item_key, other_item in other.items.items():
            if item_key not in self.items:
                raise TypeError(f"{item_key} not found")
            self.items[item_key].quantity -= other_item.quantity
            if self.items[item_key].quantity < 0:
                raise ValueError("can't have negative quantity of items")
            # If quantity is zero, remove the item
            if self.items[item_key].quantity == 0:
                del self.items[item_key]

        return self

@functools.total_ordering
@dataclasses.dataclass
class Discount:
    required_items: Basket
    discount_value: int
    removed_items: Basket  # a function that applies the discount

    def __post_init__(self):
        # Calculate the value of discount on initialization
        normal_price = sum(
            item.total_price for item in self.required_items.items.values())
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
        ValueError,TypeError
        """
        basket -= self.removed_items
        return self.discount_value

        # If we've made it here, the basket meets the discount criteria
    def __le__(self, other):
        return self.discount_value <= other.discount_value


DISCOUNTS = [
    Discount(
        required_items=Basket().create_basket("AAA"),
        removed_items=Basket().create_basket("AAA"),
        discount_value=Items.A.value.total_price*3-130
    ),
    Discount(
        required_items=Basket().create_basket("AAAAA"),
        removed_items=Basket().create_basket("AAAAA"),
        discount_value=Items.A.value.total_price*5-200
    ),
    Discount(
        required_items=Basket().create_basket("BB"),
        removed_items=Basket().create_basket("BB"),
        discount_value=Items.B.value.total_price*2-45
    ),
    Discount(
        required_items=Basket().create_basket("EE"),
        removed_items=Basket().create_basket("EEB"),
        discount_value=Items.B.value.total_price
    )
]
DISCOUNTS.sort(reverse=True)  # Now discounts are sorted in descending order of discount_value


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

    basket = Basket().create_basket(skus)
    total_discount = 0
    for discount in DISCOUNTS:
        while True:
            try:
                total_discount += discount.apply_discount(basket)
            except (ValueError, TypeError):
                break
    return basket.value + total_discount  # Final price is the sum of the remaining basket value and total discounts applied
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






