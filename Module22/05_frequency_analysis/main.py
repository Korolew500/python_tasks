def analysis(user_file):
    text_file = open(user_file, 'r')
    text = text_file.read().lower()
    text_file.close()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    symbols_set = {i: text.count(i) for i in alphabet}
    numbers = reversed(list({i for i in symbols_set.values()}))
    summ = sum([text.count(i) for i in alphabet])
    analysis_info = []

    for i_num in numbers:
        for i_sym in alphabet:
            if i_num != 0 and i_num == symbols_set[i_sym]:
                new_text = i_sym + ' ' + str(round(i_num/summ, 3)) + '\n'
                analysis_info.append(new_text)

    analysis_file = open('analysis.txt', 'w')
    analysis_file.writelines(analysis_info)
    analysis_file.close()


analysis('text.txt')
