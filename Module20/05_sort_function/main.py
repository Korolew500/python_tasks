def tpl_sort(user_tuple):

    for i in user_tuple:
        if not isinstance(i, int):
            return user_tuple

    return tuple(sorted(user_tuple))


# tpl = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))
