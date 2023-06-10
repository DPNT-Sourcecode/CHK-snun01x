from .models import Discount,Basket,Items
DISCOUNTS = [
    # | A    | 50    | 3A for 130, 5A for 200 |
    Discount(
        required_items=Basket().create_basket("A" * 3),
        removed_items=Basket().create_basket("A" * 3),
        discounted_price=130,
    ),
    Discount(
        required_items=Basket().create_basket("A" * 5),
        removed_items=Basket().create_basket("A" * 5),
        discounted_price=200,
    ),
    # | B    | 30    | 2B for 45              |
    Discount(
        required_items=Basket().create_basket("B" * 2),
        removed_items=Basket().create_basket("B" * 2),
        discounted_price=45,
    ),
    # | E    | 40    | 2E get one B free      |
    Discount(
        required_items=Basket().create_basket("EE"),
        removed_items=Basket().create_basket("EEB"),
        discounted_price=Items.E.value.price * 2,
    ),
    # | F    | 10    | 2F get one F free      |
    Discount(
        required_items=Basket().create_basket("F" * 3),
        removed_items=Basket().create_basket("F" * 3),
        discounted_price=Items.F.value.price * 2,
    ),
    #   | H    | 10    | 5H for 45, 10H for 80  |
    Discount(
        required_items=Basket().create_basket("H" * 5),
        removed_items=Basket().create_basket("H" * 5),
        discounted_price=45,
    ),
    Discount(
        required_items=Basket().create_basket("H" * 10),
        removed_items=Basket().create_basket("H" * 10),
        discounted_price=80,
    ),
    #   | K    | 80    | 2K for 150             |

    Discount(
        required_items=Basket().create_basket("K" * 2),
        removed_items=Basket().create_basket("K" * 2),
        discounted_price=150,
    ),
    #    | N    | 40    | 3N get one M free      |
    Discount(
        required_items=Basket().create_basket("N" * 3),
        removed_items=Basket().create_basket("N" * 3 + "M"),
        discounted_price=Items.N.value.price * 3,
    ),
    #     | P    | 50    | 5P for 200             |
    Discount(
        required_items=Basket().create_basket("P" * 5),
        removed_items=Basket().create_basket("P" * 5),
        discounted_price=200,
    ),
    # | Q    | 30    | 3Q for 80              |
    Discount(
        required_items=Basket().create_basket("Q" * 3),
        removed_items=Basket().create_basket("Q" * 3),
        discounted_price=80,
    ),
    # | R    | 50    | 3R get one Q free      |
    Discount(
        required_items=Basket().create_basket("R" * 3),
        removed_items=Basket().create_basket("R" * 3+"Q"),
        discounted_price=Items.R.value.price * 3,
    ),
    # | U    | 40    | 3U get one U free      |
    Discount(
        required_items=Basket().create_basket("U" * 3),
        removed_items=Basket().create_basket("U" * 4),
        discounted_price=Items.U.value.price * 3,
    ),
    # | V    | 50    | 2V for 90, 3V for 130  |
    Discount(
        required_items=Basket().create_basket("V" * 2),
        removed_items=Basket().create_basket("V" * 2),
        discounted_price=90,
    ),
    Discount(
        required_items=Basket().create_basket("V" * 3),
        removed_items=Basket().create_basket("V" * 3),
        discounted_price=130,
    ),
]
DISCOUNTS.sort(
    reverse=True
)  # Now discounts are sorted in descending order of discounted_price

