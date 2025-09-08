goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def goods_information():
    for good in goods.keys():
        summ_quantity = sum([store[goods[good]][x]['quantity']
                             for x in range(len(store[goods[good]]))])
        summ_price = sum([store[goods[good]][x]['quantity'] * store[goods[good]][x]['price']
                          for x in range(len(store[goods[good]]))])
        print(good, '— {quantity} штук, стоимость {price} рублей'.format(
            quantity=summ_quantity,
            price=summ_price))


goods_information()
