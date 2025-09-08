class Date:
    def __init__(self):
        self.s_text = '01-01-1900'
        self.data_list = self.s_text.split('-')
        self.day = '01'
        self.month = '01'
        self.year = '1900'

    def from_string(self, s_text: str) -> 'Date':
        self.s_text = s_text
        self.data_list = self.s_text.split('-')
        self.day = self.data_list[0]
        self.month = self.data_list[1]
        self.year = self.data_list[2]
        return self

    def __str__(self) -> str:
        return (f'День: {self.day}\t'
                f'Месяц: {self.month}\t'
                f'Год: {self.year}')

    def is_date_valid(self, d_text: str = '') -> bool:
        if d_text == '':
            d_text = self.s_text
        data_list = d_text.split('-')
        if (len(data_list[0]) == 2 and          # день - 2 символа
            len(data_list[1]) == 2 and          # месяц - 2 символа
            len(data_list[2]) == 4 and          # год - 4 символа
            1 <= int(data_list[2]) <= 9999 and  # год положительное число
            1 <= int(data_list[1]) <= 12 and    # месяц от 1 до 12
                                                # проверка дня (ниже)
            (((1 <= int(data_list[0]) <= 31) and int(data_list[1]) in [1, 3, 5, 7, 8, 10, 12]) or
             ((1 <= int(data_list[0]) <= 31) and int(data_list[1]) in [4, 6, 9, 11]) or
             ((1 <= int(data_list[0]) <= 28) and int(data_list[1]) == 2) or
             ((int(data_list[0]) == 29) and int(data_list[1]) == 2 and (int(data_list[2]) % 4 == 0)))):
            return True
        else:
            return False


date = Date().from_string('10-12-2077')
print(date)
print(Date().is_date_valid('10-12-2077'))
print(Date().is_date_valid('40-12-2077'))
