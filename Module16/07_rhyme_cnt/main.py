people = int(input('Кол-во человек: '))
num_count = int(input('Какое число в считалке: '))
print('Значит, выбывает каждый ' + str(num_count) + '-й человек')

people_count = []
for i in range(people):
    people_count.append(i + 1)

stop = 0
while len(people_count) != 1:
    print('\nТекущий круг людей:', people_count)
    print('Начало счёта с номера', people_count[stop])
    steps = (num_count - 1) % len(people_count)
    if (steps + stop) >= len(people_count):
        steps -= len(people_count)
    stop += steps
    print('Выбывает человек под номером', people_count[stop])
    people_count.remove(people_count[stop])
    if stop == len(people_count):
        stop = 0

print('\nОстался человек под номером', people_count[0])
