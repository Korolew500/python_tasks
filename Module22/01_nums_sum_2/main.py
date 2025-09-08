def summ_the_numbers(numbers_file, summ_file):
    user_file = open(numbers_file, 'r')
    answer_file = open(summ_file, 'w')

    summ = 0
    for i_line in user_file:
        for i_number in i_line.split():
            summ += int(i_number)
    answer_file.write(str(summ))

    user_file.close()
    answer_file.close()


summ_the_numbers('numbers.txt', 'answer.txt')
