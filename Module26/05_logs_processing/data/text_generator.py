import random
import datetime

# Изменяя N можно управлять количеством строк в файле
N = 1000


error_names = ['ValueError', 'ArithmeticError', 'AssertionError', 'ImportError', 'NameError', 'OSError']

def text_generator(logs_file):
    with open(logs_file, 'w', encoding='utf8') as file:
        for _ in range(N):
            if random.randint(1, 10) == 5:
                text = 'ERROR: ' + random.choice(error_names) + ' ' + str(datetime.datetime.today())
            else:
                text = 'COMPLETE: Данные успешно переданы.'
            file.write(text + '\n')
