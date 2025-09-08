def file_around(user_file):
    file = open(user_file, 'r')

    for i_line in file.readlines()[::-1]:
        print(i_line, end='')

    file.close()


file_around('zen.txt')
