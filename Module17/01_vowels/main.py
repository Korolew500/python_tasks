list_vowels = ['а', 'А', 'о', 'О', 'у', 'У', 'ы', 'Ы', 'э', 'Э', 'я', 'Я', 'ё', 'Ё', 'ю', 'Ю', 'и', 'И', 'е', 'Е']

user_text = input('Введите текст: ')

list_vowels_text = [letter for letter in user_text if letter in list_vowels]

print('Список гласных букв:', list_vowels_text, '\nДлина списка:', len(list_vowels_text))
