from collections import Counter

PRICES = {
    'A': [50, None, 130],
    'B': [30, 45],
    'C': [20],
    'D': [15],
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    c = Counter(skus)
