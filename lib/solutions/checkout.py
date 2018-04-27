import math
from collections import Counter, defaultdict
from operator import itemgetter

PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}

MULTI_BUYS = {
    'A': [
        {'count': 5, 'price': 200},
        {'count': 3, 'price': 130},
    ],
    'B': [
        {'count': 2, 'price': 45}
    ],
    'H': [
        {'count': 10, 'price': 80},
        {'count': 5, 'price': 45},
    ],
    'K': [
        {'count': 2, 'price': 150}
    ],
    'P': [
        {'count': 5, 'price': 200}
    ],
    'Q': [
        {'count': 3, 'price': 80}
    ],
    'V': [
        {'count': 3, 'price': 130},
        {'count': 2, 'price': 90},
    ]
}

GIFTS = {
    'E': {'sku': 'B', 'count': 2},
    'N': {'sku': 'M', 'count': 3},
    'R': {'sku': 'Q', 'count': 3}
}

BOGOFS = {
    'F': {'free': 1, 'count': 3},
    'U': {'free': 1, 'count': 4}
}

GROUP_DISCOUNTS = {
    'STXYZ': {'price': 45, 'count': 3}
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    invalid_skus = [s for s in skus if s not in PRICES.keys()]
    if invalid_skus:
        return -1

    total = 0
    c = Counter(skus)

    for skus, discount in GROUP_DISCOUNTS.items():
        prices = [(s, p) for s, p in PRICES.items() if s in skus]
        prices = sorted(prices, key=itemgetter(0))
        print(prices)

    gifts = defaultdict(int)
    for sku, count in c.items():
        if sku in GIFTS and count >= GIFTS[sku]['count']:
            gifts[GIFTS[sku]['sku']] += math.floor(count / GIFTS[sku]['count'])
        if sku in BOGOFS and count >= BOGOFS[sku]['count']:
            free = math.floor(count / BOGOFS[sku]['count']) * BOGOFS[sku]['free']
            c[sku] -= free

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
