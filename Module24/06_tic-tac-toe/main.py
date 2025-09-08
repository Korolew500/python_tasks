import random


# 1. Класс, который будет описывать одну клетку поля:
class Cell:
    def __init__(self, number):
        self.value = ' '
        self.number = number


# 2. Класс, который будет описывать поле игры.
class Board:
    def __init__(self):
        self.b_list = [Cell(i) for i in range(1, 10)]

    def info(self):
        print(f'\n  {self.b_list[0].value} | {self.b_list[1].value} | {self.b_list[2].value}')
        print(' ---|---|---')
        print(f'  {self.b_list[3].value} | {self.b_list[4].value} | {self.b_list[5].value}')
        print(' ---|---|---')
        print(f'  {self.b_list[6].value} | {self.b_list[7].value} | {self.b_list[8].value}\n')


# 3. Класс, который описывает поведение игрока:
class Player:
    def __init__(self, pl_type=0, symbol='O'):
        self.pl_type = pl_type
        self.symbol = symbol
        if self.pl_type == 0:
            self.name = random.choice([f'==Vintik-{random.randint(1, 1000)}==',
                                       f'==Shpuntik-{random.randint(1, 1000)}==',
                                       f'==Spanch-Bob-{random.randint(1, 1000)}=='])
        else:
            self.name = input('Введите свой ник: ')
            self.name = '==' + self.name + '=='

    def go(self):
        if self.pl_type == 0:
            return str(random.randint(1, 9))
        else:
            return input('Введите номер ячейки и сделайте свой ход: ')

        #  1 | 2 | 3
        # ---|---|---
        #  4 | 5 | 6
        # ---|---|---
        #  7 | 8 | 9


# 4. Класс, который управляет ходом игры:
class Game:
    def __init__(self):
        print('Добро пожаловать в крестики-нолики!')
        print('Клетки игрового поля нумеруются по порядку:')
        print('  1 | 2 | 3')
        print(' ---|---|---')
        print('  4 | 5 | 6')
        print(' ---|---|---')
        print('  7 | 8 | 9')
        self.player_1 = Player()
        type_pl_2 = input('\nСыграете сами (1) или посмотрим за битвой искусственного интеллекта (0): ')
        if type_pl_2 == '0':
            self.player_2 = Player(0, 'X')
        else:
            self.player_2 = Player(1, 'X')
        self.player = self.player_2
        self.board_1 = Board()
        self.step = 0
        self.wins = [0, 0, 0]
        self.next = '1'
        while True:
            self.one_game()
            self.info()
            self.next = input('Играем дальше? 1 - да, 0 - нет: ')
            if self.next == '0':
                print('\nОтлично поиграли!')
                break

    def info(self):
        print('\nСтатистика:')
        print(f'{self.player_1.name} победил {self.wins[0]} раз')
        print(f'{self.player_2.name} победил {self.wins[1]} раз')
        print(f'Сыграно игр в ничью: {self.wins[2]}\n')

    def one_game(self):
        self.player = self.player_1
        self.board_1 = Board()
        self.step = 0
        while True:
            if self.player == self.player_2:
                self.player = self.player_1
            elif self.player == self.player_1:
                self.player = self.player_2
            self.game_step()
            if ((self.board_1.b_list[0].value == self.board_1.b_list[1].value and
                    self.board_1.b_list[1].value == self.board_1.b_list[2].value and
                    self.board_1.b_list[2].value == self.player.symbol) or
                (self.board_1.b_list[3].value == self.board_1.b_list[4].value and
                    self.board_1.b_list[4].value == self.board_1.b_list[5].value and
                    self.board_1.b_list[5].value == self.player.symbol) or
                (self.board_1.b_list[6].value == self.board_1.b_list[7].value and
                    self.board_1.b_list[7].value == self.board_1.b_list[8].value and
                    self.board_1.b_list[8].value == self.player.symbol) or
                (self.board_1.b_list[0].value == self.board_1.b_list[3].value and
                    self.board_1.b_list[3].value == self.board_1.b_list[6].value and
                    self.board_1.b_list[6].value == self.player.symbol) or
                (self.board_1.b_list[1].value == self.board_1.b_list[4].value and
                    self.board_1.b_list[4].value == self.board_1.b_list[7].value and
                    self.board_1.b_list[7].value == self.player.symbol) or
                (self.board_1.b_list[2].value == self.board_1.b_list[5].value and
                    self.board_1.b_list[5].value == self.board_1.b_list[8].value and
                    self.board_1.b_list[8].value == self.player.symbol) or
                (self.board_1.b_list[0].value == self.board_1.b_list[4].value and
                    self.board_1.b_list[4].value == self.board_1.b_list[8].value and
                    self.board_1.b_list[8].value == self.player.symbol) or
                (self.board_1.b_list[2].value == self.board_1.b_list[4].value and
                    self.board_1.b_list[4].value == self.board_1.b_list[6].value and
                    self.board_1.b_list[6].value == self.player.symbol)):
                print(f'{self.player.name} сделал ход!')
                self.board_1.info()
                print(f'Победитель: {self.player.name}!')
                if self.player == self.player_1:
                    self.wins[0] += 1
                elif self.player == self.player_2:
                    self.wins[1] += 1
                break
            elif all(self.board_1.b_list[i].value != ' ' for i in range(9)):
                print(f'{self.player.name} сделал ход!')
                self.board_1.info()
                print('Ничья!')
                self.wins[2] += 1
                break
            print(f'{self.player.name} сделал ход!')

    def game_step(self):
        self.board_1.info()
        while True:
            try:
                self.step = int(self.player.go())
                if self.board_1.b_list[self.step - 1].value != ' ':
                    if self.player.pl_type == 0:
                        continue
                    else:
                        raise ValueError
                self.board_1.b_list[self.step - 1].value = self.player.symbol
                break
            except (ValueError, TypeError, IndexError):
                print('Ошибка. Попробуйте ввести ещё раз.')


Game()
