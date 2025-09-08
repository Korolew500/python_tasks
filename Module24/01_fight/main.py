import random


class Warrior:
    def __init__(self):
        self.life = 100

    def hit(self):
        self.life -= 20

    def info(self):
        if self.life <= 0:
            print('Воин убит.')
        else:
            print(f'У воина осталось {self.life} очков здоровья')


def war():
    loser = random.randint(0, 1)
    warriors[loser].hit()
    print(f'Воин {loser + 1} получил удар.')
    warriors[loser].info()


def main():
    print('Воин 1 и Воин 2 сошлись в битве.\n')

    while True:
        war()
        if warriors[0].life <= 0:
            print('\nВоин 2 победил!')
            break
        elif warriors[1].life <= 0:
            print('\nВоин 1 победил!')
            break
        print()


warriors = [Warrior(), Warrior()]
main()
