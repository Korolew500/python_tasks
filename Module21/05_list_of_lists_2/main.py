nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def straighten(u_list):
    fin_list = []
    for i in u_list:
        if isinstance(i, list):
            fin_list.extend(straighten(i))
        else:
            fin_list.append(i)
    return fin_list


print(straighten(nice_list))
