number_of_containers = int(input('Введите количество контейнеров: '))
containers, max_weight, count = [], 200, 0

for container in range(number_of_containers):
    while True:
        container_weight = int(input('Введите массу контейнера: '))
        if container_weight > 200:
            print('Ошибка! Вес контейнера не должен превышать 200.')
        elif container_weight > max_weight:
            print('Ошибка! Вес контейнера не должен превышать вес предыдущего контейнера')
        else:
            containers.append(container_weight)
            max_weight = container_weight
            break

new_container = int(input('Введите вес нового контейнера: '))

for cont in containers:
    count += 1
    if cont < new_container:
        print('Номер, который получит новый контейнер:', count)
        break
