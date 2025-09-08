def second_tour(user_path_file):
    first_file = open(user_path_file, 'r')
    first_info = first_file.readlines()
    first_file.close()

    numbers = []
    for i in range(len(first_info)):
        if i != 0:
            first_info[i] = first_info[i].split()
            if int(first_info[i][2]) > int(first_info[0]):
                numbers.append(first_info[i][2])

    second_info = []
    for i_num in sorted(numbers, reverse=True):
        for j_info in first_info[1:]:
            if j_info[2] == i_num:
                new_text = ('\n' +
                            str(len(second_info) + 1) + ') ' +
                            j_info[1][0] + '. ' +
                            j_info[0] + ' ' +
                            i_num)
                second_info.append(new_text)
    second_info.insert(0, str(len(second_info)))

    second_file = open('second_tour.txt', 'w')
    second_file.writelines(second_info)
    second_file.close()


second_tour('first_tour.txt')
