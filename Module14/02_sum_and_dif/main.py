def summ_digits(num):
    summ = 0
    for figure in str(num):
        summ += int(figure)
    return summ


def quantity_digits(num):
    return len(str(num))


number = int(input('\nВведите число: '))

sum_digits = summ_digits(number)
quantity_dig = quantity_digits(number)
difference_numbers = sum_digits - quantity_dig

print('\nСумма цифр:', sum_digits)
print('Количество цифр в числе:', quantity_dig)
print('Разность суммы и количества цифр:', difference_numbers)
