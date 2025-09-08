import random


names = ['Иван', 'Пётр', 'Сергей', 'Николай', 'Анна', 'Ольга', 'Гарри', 'Бэлла',
         'Алексей', 'Мария', 'Иван', 'Елена', 'Дмитрий', 'Анна', 'Сергей',
         'София', 'Анатолий', 'Екатерина', 'Михаил', 'Татьяна', 'Артем',
         'Виктория', 'Григорий', 'Марина', 'Павел', 'Юлия', 'Сара']


class Home:
    def __init__(self):
        self.food = 50
        self.money = 0

    def info(self):
        print(f'В холодильнике {self.food} еды\nВ тумбочке {self.money} денег\n')


class Human:
    def __init__(self, home=Home()):
        self.name = random.choice(names)
        self.satiety = 50
        self.home = home

    def eat(self):
        print(f'{self.name} ест')
        self.satiety += 2
        self.home.food -= 1
        self.info()

    def info(self):
        print(f'{self.name} имеет сытость {self.satiety}')
        self.home.info()

    def work(self):
        print(f'{self.name} работает')
        self.satiety -= 1
        self.home.money += 2
        self.info()

    def game(self):
        print(f'{self.name} играет')
        self.satiety -= 1
        self.info()

    def shop(self):
        print(f'{self.name} идет в магазин за едой')
        self.home.food += 2
        self.home.money -= 1
        self.info()

    def go(self):
        num = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.home.food < 10:
            self.shop()
        elif self.home.money < 50:
            self.work()
        elif num == 1:
            self.work()
        elif num == 2:
            self.eat()
        else:
            self.game()


home_1 = Home()
human_1 = Human(home_1)
human_2 = Human(home_1)


def year_live():
    print(f'\n{human_1.name} и {human_2.name} будут жить в одном доме целый год!\n')
    for day in range(1, 366):
        print(f'День {day}\n')
        human_1.go()
        human_2.go()
        if human_1.satiety <= 0:
            print(f'\n{human_1.name} постигла голодная смерть')
            break
        if human_2.satiety <= 0:
            print(f'\n{human_2.name} постигла голодная смерть')
            break
    print('Конец')


year_live()
