guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


def main():
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    command = input('Гость пришёл или ушёл? ')
    if command == 'ушёл':
        get_out()
    elif command == 'пришёл':
        get_in()
    elif command == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
    else:
        print('Опечатка, повторите запрос.')
        main()


def get_out():
    name = input('Имя гостя: ')
    if name in guests:
        guests.remove(name)
        print('Пока, ' + name + '!')
        main()
    else:
        print('Ошибка в имени.')
        main()


def get_in():
    name = input('Имя гостя: ')
    if len(guests) < 6:
        guests.append(name)
        print('Привет, ' + name + '!')
        main()
    else:
        print('Прости, ' + name + ', но мест нет.')
        main()


main()
