import random


def while_700(result_file):
    summ = 0
    try:
        while summ < 700:
            num = int(input('Введите число: '))
            if random.randint(1, 13) == 13:
                raise ValueError
            with open(result_file, 'a', encoding='utf-8') as result_open_file:
                result_open_file.write(str(num) + '\n')
            summ += num
    except ValueError or TypeError:
        print('Вас постигла неудача!')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    finally:
        print(f'Содержимое файла {result_file}:')
        with open(result_file, 'r', encoding='utf-8') as res_file:
            for i_line in res_file.readlines():
                print(i_line.strip('\n'))


while_700('out_file.txt')
