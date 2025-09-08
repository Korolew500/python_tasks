import re

if __name__ == '__main__':
    telephone_numbers = ['9999999999', '999999-999', '99999x9999',
                         '9999999999', '999999-999', '99999x9999',
                         '9999999999', '999999-999', '99999x9999',
                         '9999999999', '999999-999', '99999x9999']
    format_num = r'[89]\d{9}'

    for i, i_number in enumerate(telephone_numbers):
        if i_number in re.findall(format_num, i_number):
            print(f'{i + 1} номер: всё в порядке')
        else:
            print(f'{i + 1} номер: не подходит')
