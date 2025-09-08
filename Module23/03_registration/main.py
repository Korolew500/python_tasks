def reg_check():
    with open('registrations.txt', 'r', encoding='utf-8') as reg_file:
        with open('registrations_good.log', 'a', encoding='utf-8') as good_file:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
                for i_line in reg_file.readlines():
                    reg_data = i_line.strip('\n').split()
                    try:
                        if len(reg_data) != 3:
                            raise IndexError
                        elif not reg_data[0].isalpha():
                            raise NameError
                        elif not ('@' in reg_data[1]) or not ('.' in reg_data[1]):
                            raise SyntaxError
                        elif not (10 <= int(reg_data[2]) <= 99):
                            raise ValueError
                        else:
                            good_file.write(i_line)
                    except IndexError:
                        bad_file.write(i_line.strip('\n') + '\t\tНЕ присутствуют все три поля\n')
                    except NameError:
                        bad_file.write(i_line.strip('\n') + '\t\tПоле «Имя» содержит НЕ только буквы\n')
                    except SyntaxError:
                        bad_file.write(i_line.strip('\n') + '\t\tПоле «Имейл» НЕ содержит @ и . (точку)\n')
                    except ValueError:
                        bad_file.write(i_line.strip('\n') + '\t\tПоле «Возраст» НЕ является числом от 10 до 99\n')
    print('Содержимое файла registrations_bad.log:')
    with open('registrations_bad.log', 'r', encoding='utf-8') as bad_log:
        for i_bad in bad_log:
            print(i_bad.strip('\n'))
    print('\nСодержимое файла registrations_good.log:')
    with open('registrations_good.log', 'r', encoding='utf-8') as good_log:
        for i_good in good_log:
            print(i_good.strip('\n'))


reg_check()
