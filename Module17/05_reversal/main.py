string_user = input('Введите строку: ')

hh_string_user = string_user[(len(string_user) - string_user[::-1].index('h') - 2):string_user.index('h'):-1]

print('Развёрнутая последовательность между первым и последним h:', hh_string_user)
