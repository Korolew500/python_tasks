count = int(input('Введите количество заказов: '))
orders = dict()

for i in range(count):
    text = str(i + 1) + ' заказ: '
    orders_i = input(text).split()
    orders_i[2] = int(orders_i[2])
    if orders_i[0] not in orders:
        orders[orders_i[0]] = {orders_i[1]: orders_i[2]}
    elif orders_i[1] in orders[orders_i[0]]:
        orders[orders_i[0]][orders_i[1]] += orders_i[2]
    else:
        orders[orders_i[0]].update({orders_i[1]: orders_i[2]})

for i in sorted(orders.keys()):
    print(i + ':')
    for j in sorted(orders[i].keys()):
        print('\t' + j + ': ' + str(orders[i][j]))
