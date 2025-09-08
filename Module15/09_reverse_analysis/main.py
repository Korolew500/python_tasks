# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]

for count in range(len(numbers_list) - 1, -1, -1):
    if numbers_list[count] % 2 == 0:
        numbers_list.append(numbers_list[count])
    numbers_list.pop(count)

for number in range(len(numbers_list)):
    min_num, num_count = 9e50, 0
    for i in range(number, len(numbers_list)):
        if numbers_list[i] < min_num:
            min_num = numbers_list[i]
            num_count = i
    cash_num = min_num
    numbers_list.pop(num_count)
    numbers_list.insert(0, cash_num)

print('Обработанный список:', numbers_list)
