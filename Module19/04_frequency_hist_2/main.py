u_text = input('Введите текст: ')


def character_frequency(user_text):
    dict_1 = {x: user_text.count(x) for x in user_text}
    dict_2 = {}

    for i in dict_1.keys():
        if dict_1[i] in dict_2:
            dict_2[dict_1[i]].append(i)
        else:
            dict_2[dict_1[i]] = [i]

    print('\nОригинальный словарь частот:')
    for i in dict_1.keys():
        print(i, ':',  dict_1[i])

    print('\nИнвертированный словарь частот:')
    for i in dict_2.keys():
        print(i, ':',  dict_2[i])


character_frequency(u_text)
