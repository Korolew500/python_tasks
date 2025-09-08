number = int(input('Введите число: '))
num_list = []
for num in range(1, number + 1, 2):
    num_list.append(num)
print('Список из нечетных чисел от 1 до N:', num_list)
