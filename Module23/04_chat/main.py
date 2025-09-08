import datetime


def main_chat():
    user_login = input('Введите логин: ')
    while True:
        print('\n1 - Посмотреть текущий текст чата\n'
              '2 - Отправить сообщение\n'
              '0 - Выход из чата\n'
              'Выберите действие: ')
        action = input()
        if action == '1':
            with open('chat.txt', 'r', encoding='utf-8') as chat_r:
                print()
                for i_line in chat_r.readlines():
                    print(i_line.strip('\n'))
        elif action == '2':
            with open('chat.txt', 'a', encoding='utf-8') as chat_w:
                message = input('\nВведите сообщение:\n')
                chat_w.write(f'{user_login}, {datetime.datetime.now()}\n')
                chat_w.write(f'{message}\n\n')
        elif action == '0':
            break


main_chat()
