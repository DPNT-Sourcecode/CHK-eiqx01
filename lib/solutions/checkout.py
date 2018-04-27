import string
from collections import Counter

PRICES = {
    'A': [50, 100, 130],
    'B': [30, 45],
    'C': [20],
    'D': [15],
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    c = Counter(skus.upper())
    for sku, count in c.items():
        if sku not in 'ABCD':
            continue
        prices = PRICES[sku]
        if count <= len(prices):
            sum_ = prices[count - 1]
        else:
            sum_ = prices[-1] / len(prices) * count
        total += sum_
    return total

