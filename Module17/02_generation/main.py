number = int(input('Введите длину списка: '))

list_numbers = [list_num % 5 if list_num % 2 == 1 else 1 for list_num in range(number)]

print('Результат:', list_numbers)
