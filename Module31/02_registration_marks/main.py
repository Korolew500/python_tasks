import re

data_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

if __name__ == '__main__':
    auto_fiz = re.findall(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', data_numbers)
    auto_tax = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', data_numbers)
    print('Список номеров частных автомобилей:', auto_fiz)
    print('Список номеров такси:', auto_tax)
