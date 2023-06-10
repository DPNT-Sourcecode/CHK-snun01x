# noinspection PyUnusedLocal
# skus = unicode string
import re
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
        raise TypeError(f'Expected {skus} to match {pattern}')

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
    valide_skus(skus)
    raise NotImplementedError()

