site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(dict_name, key_name, count):
    for i_key, i_value in dict_name.items():
        if i_key == key_name:
            return i_value
        elif (isinstance(i_value, dict)) and count > 1:
            answer = search(i_value, key_name, count - 1)
            if answer is not None:
                return answer
    return None


user_key = input('Введите искомый ключ: ')
depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
user_count = 1000
if depth == 'y':
    user_count = int(input('Введите максимальную глубину: '))

print('Значение ключа:', search(site, user_key, user_count))
