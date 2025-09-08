count = int(input('Сколько будет чисел в списке? '))
list_num = []

for num in range(count):
    elem_num = int(input('Введите число: '))
    list_num.append(elem_num)

print('Изначальный список:', list_num)

for number in range(count):
    max_num, num_count = -9e50, 0
    for i in range(number, count):
        if list_num[i] > max_num:
            max_num = list_num[i]
            num_count = i
    cash_num = max_num
    list_num.pop(num_count)
    list_num.insert(0, cash_num)

print('Отсортированный список:', list_num)
