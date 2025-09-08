def check(count_check):
    for j in range(count_check):
        if numbers[j] == numbers[((j + 1) * -1)]:
            continue
        else:
            return False
    return True


numbers, new_numbers, count_num = [], [], 0

count = int(input('Количество чисел: '))
for i in range(count):
    num = int(input('Число: '))
    numbers.append(num)
print('\nПоследовательность:', numbers)

for i in range(count):
    if check(count):
        break
    else:
        if i == 0:
            numbers.append(numbers[i])
            new_numbers.append(numbers[i])
        else:
            numbers.insert((i * -1), numbers[i])
            new_numbers.insert((i * -1), numbers[i])
        count_num += 1

print('Нужно приписать чисел:', count_num)
print('Сами числа:', new_numbers)
