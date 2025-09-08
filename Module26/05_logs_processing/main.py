# TODO здесь писать код
from os import path
from data.text_generator import *


def error_log_generator(input_file):
    if not path.exists(input_file):
        text_generator(path.abspath(path.join('data', 'work_logs.txt')))
    with open(input_file, 'r',  encoding='utf8') as errors:
        for error_l in errors.readlines():
            if error_l[:5] == 'ERROR':
                yield error_l


# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = path.join('data', 'work_logs.txt')
output_file_path = path.join('data', 'output.txt')
# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/

with open(output_file_path, 'w', encoding='utf8') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")
