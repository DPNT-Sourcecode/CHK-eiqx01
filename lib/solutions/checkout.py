import math
import string
from collections import Counter, defaultdict

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

MULTI_BUYS = {
    'A': [
        {'count': 5, 'price': 200},
        {'count': 3, 'price': 130},
    ],
    'B': [
        {'count': 2, 'price': 45}
    ]
}

GIFTS = {
    'E': {'sku': 'B', 'count': 2}
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    invalid_skus = [s for s in skus if s not in 'ABCDE']
    if invalid_skus:
        return -1

    total = 0
    c = Counter(skus)

    gifts = defaultdict(int)
    for sku, count in c.items():
        if sku in GIFTS and count >= GIFTS[sku]['count']:
            gifts[GIFTS[sku]['sku']] += math.floor(count / GIFTS[sku]['count'])
    for sku, count in c.items():
        if sku in gifts:
            count = max(0, count - gifts[sku])
        price = PRICES[sku]
        if sku in MULTI_BUYS:
            remainder = count
            sum_ = 0
            for multi_buy in MULTI_BUYS[sku]:
                if remainder >= multi_buy['count']:
                    sum_ += multi_buy['price'] * math.floor(remainder / multi_buy['count'])
                    remainder = remainder % multi_buy['count']
            sum_ += remainder * price
        else:
            sum_ = count * price
        total += sum_

    return total
