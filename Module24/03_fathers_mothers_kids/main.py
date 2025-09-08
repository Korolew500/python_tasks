import random


names = ['Иван', 'Пётр', 'Сергей', 'Николай', 'Анна', 'Ольга', 'Гарри', 'Бэлла',
         'Алексей', 'Мария', 'Иван', 'Елена', 'Дмитрий', 'Анна', 'Сергей',
         'София', 'Анатолий', 'Екатерина', 'Михаил', 'Татьяна', 'Артем',
         'Виктория', 'Григорий', 'Марина', 'Павел', 'Юлия', 'Сара']


class Parent:
    def __init__(self):
        self.name = random.choice(names)
        self.age = random.randint(20, 30)
        self.kids = [Kid(self.age) for _ in range(random.randint(1, 2))]

    def info(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет.\nМои дети:')
        for j, i_kid in enumerate(self.kids):
            print(f'\t{j + 1}) {i_kid.name}, {i_kid.age} лет - {i_kid.hunger} и {i_kid.emotions}')

    def calm(self, number_kid):
        self.kids[number_kid].emotions = 'спокоен'

    def feed(self, number_kid):
        self.kids[number_kid].hunger = 'ребёнок сыт'


class Kid:
    def __init__(self, parent_age):
        self.name = random.choice(names)
        self.age = random.randint(3, parent_age - 16)
        self.hunger = random.choice(['ребёнок голоден', 'ребёнок сыт', 'ребёнок хочет вкусняшек'])
        self.emotions = random.choice(['спокоен', 'боится', 'плачет'])


def main():
    parents = [Parent(), Parent(), Parent()]
    print('\nСпасите родителей!')
    print('(Все действия задаются цифрами)')

    while True:
        try:
            for i, i_parent in enumerate(parents):
                print(f'\n{i + 1}) ', end='')
                i_parent.info()
            parent = int(input('\nКакому родителю поможем? Введите номер родителя: '))
            kid = int(input('Какому ребенку родителя поможем? Введите номер ребенка: '))
            action = int(input('Что будем делать? Покормить (0) или успокоить (1): '))
            if action == 0:
                parents[parent - 1].feed(kid - 1)
                print('Покормили!')
            elif action == 1:
                parents[parent - 1].calm(kid - 1)
                print('Успокоили!')

            action_2 = int(input('Продолжим? Да (1) или Нет (0): '))
            if action_2 == 0:
                break

        except TypeError and ValueError:
            print('Попробуйте ещё раз')

        if (all(j.hunger == 'ребёнок сыт' for i in parents for j in i.kids) and
                all(j.emotions == 'спокоен' for i in parents for j in i.kids)):
            print('\nУ нас получилось!')
            break


main()
