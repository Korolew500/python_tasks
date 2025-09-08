import zipfile


def statistic(text):
    symbols = {i for i in user_text}
    sym_set = {sym: text.count(sym) for sym in symbols}
    numbers = sorted(set(sym_set.values()), reverse=True)

    static = []
    for i_value in numbers:
        for j_elem in sym_set:
            if sym_set[j_elem] == i_value:
                static.append(j_elem + '-' + str(sym_set[j_elem]) + '\n')

    stat_file = open('statistic.txt', 'w', encoding='utf-8')
    stat_file.writelines(static)
    stat_file.close()


user_file = zipfile.ZipFile('voyna-i-mir.zip', 'r').open('voyna-i-mir.txt')
user_text = user_file.read().decode('utf-8')
user_file.close()

statistic(user_text)
