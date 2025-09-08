word, new_word = input('Введите слово: '), ''

for letter in word:
    new_word = letter + new_word

if word == new_word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
