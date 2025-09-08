import os


def read_people_file(path_file):
    return_file = []
    with open(path_file, 'r', encoding='utf-8') as open_file:
        print('Содержимое файла ' + path_file.split(os.sep)[-1] + ':')
        for i_line in open_file.readlines():
            name = i_line.strip('\n')
            print(name)
            return_file.append(name)
        print()
        return return_file[:]


def count_names(names_list):
    summ = 0
    for i_num in range(len(names_list)):
        try:
            if len(names_list[i_num]) < 3:
                raise TypeError
        except TypeError:
            print(f'Ошибка: менее трёх символов в строке {i_num + 1}.')
            with open(os.path.join('logs', 'error.log'), 'a', encoding='utf-8') as log_file:
                log_file.write(f'Ошибка: менее трёх символов в строке {i_num + 1} в файле '
                               f'{os.path.abspath(os.path.join('people', 'people.txt'))}')
        finally:
            summ += len(names_list[i_num])
    return summ


print(f'Общее количество символов: '
      f'{count_names(read_people_file(os.path.join('people', 'people.txt')))}'
      f'.')
