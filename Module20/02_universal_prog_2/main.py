def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def cripto(user_object):
    return [value_i for key_i, value_i in enumerate(user_object) if key_i > 1 and is_prime(key_i)]


object_1 = 'О Дивный Новый мир!'

print(cripto(object_1))
