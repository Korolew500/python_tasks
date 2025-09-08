import random
import sys


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    return int(OneDay())


class OneDay:
    def __init__(self):
        self.__karma = random.randint(1, 7)
        self.__exc = random.randint(1, 10)
        self.__exc_obj = random.choice([
                                        KillError,
                                        DrunkError,
                                        CarCrashError,
                                        GluttonyError,
                                        DepressionError
        ])

    def __int__(self):
        if self.__exc == 10:
            raise self.__exc_obj
        else:
            return self.__karma


def cycle():
    with open('karma.log', 'w', encoding='utf-8') as log_file:
        day = 0
        karma = 0
        while True:
            day += 1
            try:
                new_karma = one_day()
                karma += new_karma
                print(f'День {day}. Добавлено кармы: {new_karma}. Всего кармы: {karma}.')
            except (
                    KillError,
                    DrunkError,
                    CarCrashError,
                    GluttonyError,
                    DepressionError
            ):
                name_ex = sys.exc_info()[0].__name__
                log_file.write(f'День {day}. Произошла ошибка {name_ex}\n')
                print(f'День {day}. Произошла ошибка {name_ex}. Добавлена запись в karma.log')
            if karma >= 500:
                print('Цель достигнута!')
                break


cycle()
