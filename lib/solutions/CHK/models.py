
from __future__ import annotations

import dataclasses
import functools
from enum import Enum
from typing import Dict


@functools.total_ordering
@dataclasses.dataclass
class Discount:
    required_items: Basket
    # discounted_price = price to charge customer for discount
    discounted_price: int
    removed_items: Basket  # a function that applies the discount

    @property
    def total_discounted_price(self):
        """
        Returns
        -------
        Real cost to supermarket (value of removed_items - discounted price)
        """
        return self.removed_items.value - self.discounted_price

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
        return self.discounted_price

        # If we've made it here, the basket meets the discount criteria

    def __le__(self, other):
        return self.total_discounted_price <= other.total_discounted_price



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



class Basket:
    _items: Dict[str, Item]

    @property
    def value(self):
        return sum([item.total_price for item in self.items.values()])

    @property
    def items(self) -> Dict[str, Item]:
        if not hasattr(self, "_items"):
            self._items = {}
        return self._items

    def create_basket(self, skus):
        from .utils import combine_skus_duplicates
        combined = combine_skus_duplicates(skus)
        for key, quantity in combined.items():
            item = Items[key].value
            self.items[key] = Item(key=key, quantity=quantity, price=item.total_price)
        return self

    def __sub__(self, other: Basket):
        """Subtracts another Basket instance from this one."""
        if not isinstance(other, Basket):
            raise TypeError(f"Unsupported operand type for -: {type(other)}")
        # VALIDATE FIRST
        for item_key, other_item in other.items.items():
            if item_key not in self.items:
                raise TypeError(f"{item_key} not found")
            result = self.items[item_key].quantity - other_item.quantity
            if result < 0:
                raise ValueError("can't have negative quantity of items")
        # APPLY
        for item_key, other_item in other.items.items():
            result = self.items[item_key].quantity - other_item.quantity
            self.items[item_key].quantity = result

            # If quantity is zero, remove the item
            if self.items[item_key].quantity == 0:
                del self.items[item_key]

        return self

class Items(Enum):
    A = Item("A", 50)
    B = Item("B", 30)
    C = Item("C", 20)
    D = Item("D", 15)
    E = Item("E", 40)
    F = Item("F", 10)
    G = Item("G", 20)
    H = Item("H", 10)
    I = Item("I", 35)
    J = Item("J", 60)
    K = Item("K", 80)
    L = Item("L", 90)
    M = Item("M", 15)
    N = Item("N", 40)
    O = Item("O", 10)
    P = Item("P", 50)
    Q = Item("Q", 30)
    R = Item("R", 50)
    S = Item("S", 30)
    T = Item("T", 20)
    U = Item("U", 40)
    V = Item("V", 50)
    W = Item("W", 20)
    X = Item("X", 90)
    Y = Item("Y", 10)
    Z = Item("Z", 50)


