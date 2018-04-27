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
        {'count': 3, 'price': 130},
        {'count': 4, 'price': 200},
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
    
    total = 0
    c = Counter(skus)
    gifts = defaultdict(int)
    for sku, count in c.items():
        g = GIFTS.get(sku)
        if g and count >= g.count:
            gifts[g.sku] = math.floor(count / g.count)
    for sku, count in c.items():
        if sku not in 'ABCD':
            return -1
        price = PRICES[sku]
        multi_buy = MULTI_BUYS.get(sku)
        if multi_buy and count >= multi_buy['count']:
            groups = math.floor(count / multi_buy['count'])
            remainder = count % multi_buy['count']
            sum_ = groups * multi_buy['price'] + remainder * price
        else:
            sum_ = count * price
        total += sum_

    return total
