skates, people, summ = [], [], 0

skates_count = int(input('Кол-во коньков: '))
for i in range(skates_count):
    print('Размер ' + str(i + 1) + '-й пары: ', end='')
    size = int(input(''))
    skates.append(size)

people_count = int(input('\nКол-во людей: '))
for i in range(people_count):
    print('Размер ноги ' + str(i + 1) + '-го человека: ', end='')
    size = int(input(''))
    people.append(size)

for i in skates:
    flag_count = False
    for j in people:
        if i == j:
            people.remove(j)
            summ += 1
            break

print('Наибольшее кол-во людей, которые могут взять ролики:', summ)
