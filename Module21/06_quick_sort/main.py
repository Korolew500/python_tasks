import random


def sort(user_list):

    left_list, center_list, right_list, right_num = [], [], [], user_list[-1]

    for i in user_list:
        if i == right_num:
            center_list.append(i)
        elif i < right_num:
            left_list.append(i)
        else:
            right_list.append(i)

    if len(left_list) > 1:
        left_list = sort(left_list)

    if len(right_list) > 1:
        right_list = sort(right_list)

    left_list.extend(center_list)
    left_list.extend(right_list)
    return left_list


print(sort([random.randint(1, 10) for _ in range(20)]))
