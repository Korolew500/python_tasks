violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


def total_songs():
    num, total_length = 1, 0
    quantity = int(input('Сколько песен выбрать? '))
    while quantity >= num:
        text = 'Название ' + str(num) + ' песни: '
        song = input(text)
        if song in violator_songs:
            total_length += violator_songs[song]
            num += 1
        else:
            print('Опечатка в названии или такой песни нет.')
    return round(total_length, 2)


print('\nОбщее время звучания песен:', total_songs(), 'минуты')
