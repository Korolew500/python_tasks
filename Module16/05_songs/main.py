violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count = int(input('Сколько песен выбрать? '))
summ = 0
for i in range(count):
    print('Название ' + str(i + 1) + '-й песни: ', end='')
    name_song = input('')
    for song in violator_songs:
        if name_song == song[0]:
            summ += song[1]
            break

print('Общее время звучания песен: ', summ, 'минуты')
