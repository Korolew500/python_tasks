import random


class Student:
    def __init__(self):
        self.fi = (random.choice(['Иван', 'Пётр', 'Сергей', 'Николай', 'Анна', 'Ольга', 'Гарри', 'Бэлла',
                                  'Алексей', 'Мария', 'Иван', 'Елена', 'Дмитрий', 'Анна', 'Сергей',
                                  'София', 'Анатолий', 'Екатерина', 'Михаил', 'Татьяна', 'Артем',
                                  'Виктория', 'Григорий', 'Марина', 'Павел', 'Юлия', 'Сара']) + ' ' +
                   random.choice(['Шевчук', 'Блэк', 'Поттер', 'Ладко', 'Смит', 'Лаплас', 'Ларлам',
                                  'Коннор', 'Мартинез', 'Джордон', 'Кэрроу', 'Трон', 'Зелински']))

        self.group = (random.choice(['СР', 'МТ', 'ИТ', 'ЮР']) + '-' +
                      str(random.randint(20, 24)) + '-' +
                      str(random.randint(301, 350)))

        self.grade = [random.randint(40, 100) for _ in range(5)]


students_list = [Student() for _ in range(10)]

while True:
    for i in range(len(students_list) - 1):

        if (sum(students_list[i].grade)/len(students_list[i].grade)
                > sum(students_list[i + 1].grade)/len(students_list[i + 1].grade)):
            students_list[i], students_list[i + 1] = students_list[i + 1], students_list[i]

    if all(sum(students_list[i].grade)/len(students_list[i].grade) <=
           sum(students_list[i + 1].grade)/len(students_list[i + 1].grade)
           for i in range(len(students_list) - 1)):
        break

print('Список студентов:')
for i, stud in enumerate(students_list):
    print(f'{i + 1}) {stud.fi} из группы {stud.group} - '
          f'cредняя успеваемость {sum(stud.grade)/len(stud.grade)}')
