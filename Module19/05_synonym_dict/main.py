def synonym():
    word = input('Введите слово: ').lower()
    if word in couple_words.keys():
        print('Синоним: ', couple_words[word])
    elif word in couple_words.values():
        for coup in couple_words.keys():
            if couple_words[coup] == word:
                print('Синоним: ', coup)
    else:
        print('Такого слова в словаре нет.')
        synonym()


couple = int(input('Введите количество пар слов: '))
couple_words = {}
for i in range(couple):
    text = str(i + 1) + ' пара: '
    couple_i = input(text).lower().split(' - ')
    couple_words.update({couple_i[0]: couple_i[1]})

synonym()
