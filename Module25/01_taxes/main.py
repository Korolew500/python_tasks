class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return round(self.worth / 1000, 2)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return round(self.worth / 200, 2)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return round(self.worth / 500, 2)


def main_tax():
    print('Добрый день!')
    while True:
        command = input('\nНалог на какое имущество необходимо рассчитать?\n'
                        '1 - на квартиру\n'
                        '2 - на машину\n'
                        '3 - на дачу\n'
                        '0 - выход\n')
        if command == '0':
            print('Счастливо!')
            break
        money = input('Сколько денег имеется? ')
        price = input('Сколько стоит имущество? ')

        try:
            money = int(money)
            price = int(price)
            if command == '1':
                obj = Apartment(price)
            elif command == '2':
                obj = Car(price)
            elif command == '3':
                obj = CountryHouse(price)
            else:
                raise ValueError
        except (ValueError, TypeError):
            print('Введённые данные содержат ошибку, попробуйте ещё раз.')
            continue

        tax = obj.tax()
        print(f'Необходимо заплатить налог в размере {tax} рублей.')
        if tax <= money:
            print('Денег хватает.')
        else:
            print(f'Нехватает {tax - money} рублей.')


main_tax()
