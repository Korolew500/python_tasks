def encryption(text, num):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
                'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ',
                'э', 'ю', 'я']
    return ''.join([(alphabet[alphabet.index(i) + num - (33 - num + 1)]
                     if alphabet.index(i) >= (33 - num)
                     else alphabet[alphabet.index(i) + num]) for i in text])


message = input('Введите сообщение: ')
number = int(input('Введите сдвиг: '))

print('Зашифрованное сообщение:', encryption(message, number))
