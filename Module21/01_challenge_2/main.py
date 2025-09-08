def counting_up(num):
    if num <= 1:
        print(1)
        return 1
    new_num = counting_up(num - 1) + 1
    print(new_num)
    return new_num


user_num = int(input('Введите num: '))
counting_up(user_num)
