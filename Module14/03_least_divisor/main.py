def smallest_divisor(num):
    for divisor in range(2, num + 1):
        if num % divisor == 0:
            return divisor


number = int(input('\nВведите число: '))
while number < 2:
    number = int(input('Ошибка! Введите число больше 1: '))

smallest_div = smallest_divisor(number)
print('Наименьший делитель, отличный от единицы:', smallest_div)
