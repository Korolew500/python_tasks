list_num = []
positions = int(input('Сколько элементов в списке: '))

for pos in range(positions):
    element = int(input('Введите элемент списка: '))
    list_num.append(element)

shift = int(input('На сколько позиций сдвигать вправо? '))


print('Изначальный список:', list_num)

for _ in range(shift):
    list_num.insert(0, list_num[len(list_num) - 1])
    list_num.pop(len(list_num) - 1)

print('Сдвинутый список:', list_num)
