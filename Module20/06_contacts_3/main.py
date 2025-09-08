def main():
    while True:
        print('Текущий словарь контактов:', telephone_dict)
        print(
            'Введите номер действия: '
            '\n\t1. Добавить контакт'
            '\n\t2. Найти человека'
        )
        action = int(input(''))
        if action == 1:
            add_a_contact()
        elif action == 2:
            find_a_person()
        else:
            print('Ошибка, доступны действия 1 и 2\n')


def add_a_contact():
    new_name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
    if new_name not in telephone_dict:
        new_number = int(input('Введите номер телефона: '))
        telephone_dict[new_name] = new_number
    else:
        print('Такой человек уже есть в контактах.')
    main()


def find_a_person():
    search_name = input('Введите фамилию для поиска:  ')
    count = 0
    for i_key, i_value in telephone_dict.items():
        if i_key[1].lower() == search_name.lower():
            print(i_key[0], i_key[1], i_value)
            count = 1
    if count == 0:
        print('Не найдено.')
    main()


telephone_dict = {('Иван', 'Иванов'): 1234567890, ('Петр', 'Петров'): 987654321}
main()
