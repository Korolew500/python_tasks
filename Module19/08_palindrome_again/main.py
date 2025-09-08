u_text = input('Введите строку: ')


def palindrome_is_possible(user_text):
    text = set(user_text)
    count = 0
    for i in text:
        if user_text.count(i) % 2 == 1:
            count += 1
    if count < 2:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')


palindrome_is_possible(u_text)
