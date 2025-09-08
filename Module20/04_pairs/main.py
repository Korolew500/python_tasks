import random

list_1 = [random.randint(0, 100) for _ in range(10)]

list_2 = [i for i in zip([j for j in list_1[::2]], [k for k in list_1[1::2]])]

print('Оригинальный список:', list_1)
print('Новый список:', list_2)
