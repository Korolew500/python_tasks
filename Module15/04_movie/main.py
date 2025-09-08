films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

count = int(input('Сколько фильмов хотите добавить? '))
new_films = []

for film in range(count):
    new_film = input('Введите название фильма: ')
    if new_film in films:
        new_films.append(new_film)
    else:
        print('Ошибка: фильма', new_film, 'у нас нет :(')

print('Ваш список любимых фильмов:', new_films)
