# noinspection PyUnusedLocal
# skus = unicode string

def validate_skus(skus):
    pass

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

