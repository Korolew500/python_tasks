import random


class Water:
    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if other.name == 'Вода':
            return Water()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Воздух':
            return Storm()
        elif other.name == 'Земля':
            return Dirt()


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Вода':
            return Steam()
        elif other.name == 'Огонь':
            return Fire()
        elif other.name == 'Воздух':
            return Lightning()
        elif other.name == 'Земля':
            return Lava()


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Вода':
            return Storm()
        elif other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Воздух':
            return Air()
        elif other.name == 'Земля':
            return Dust()


class Eight:
    def __init__(self):
        self.name = 'Земля'

    def __add__(self, other):
        if other.name == 'Вода':
            return Dirt()
        elif other.name == 'Огонь':
            return Lava()
        elif other.name == 'Воздух':
            return Dust()
        elif other.name == 'Земля':
            return Eight()


class Storm:
    def __init__(self):
        self.name = 'Шторм'


class Steam:
    def __init__(self):
        self.name = 'Пар'


class Dirt:
    def __init__(self):
        self.name = 'Грязь'


class Lava:
    def __init__(self):
        self.name = 'Лава'


class Lightning:
    def __init__(self):
        self.name = 'Молния'


class Dust:
    def __init__(self):
        self.name = 'Пыль'


def main():
    try:
        print('\nВ наличии имеются следующие элементы:\n'
              '1) Вода\n2) Земля\n3) Огонь\n4) Воздух\n')
        summand_1 = input('Введите номер первого слагаемого: ')
        summand_2 = input('Введите номер второго слагаемого: ')

        if summand_1 == '1':
            summand_1 = Water()
        elif summand_1 == '2':
            summand_1 = Eight()
        elif summand_1 == '3':
            summand_1 = Fire()
        elif summand_1 == '4':
            summand_1 = Air()
        else:
            raise ValueError

        if summand_2 == '1':
            summand_2 = Water()
        elif summand_2 == '2':
            summand_2 = Eight()
        elif summand_2 == '3':
            summand_2 = Fire()
        elif summand_2 == '4':
            summand_2 = Air()
        else:
            raise ValueError

        summ = summand_1 + summand_2
        print(f'\nМы получили элемент "{summ.name}"!')

    except ValueError:
        print('\nЭксперимент не удался!')


while True:
    main()

    if random.randint(1, 10) == 5:
        print('По рабочей области пробежала кошка,\n'
              'Всё пролилось, перемешалось, загорелось и взорвалось!\n'
              'На месте происшествия нашли 30 кг золота..\n'
              'Цель исследований достигнута! Ура!\n'
              '(Как именно получили золото, никто не знает)')
        break
