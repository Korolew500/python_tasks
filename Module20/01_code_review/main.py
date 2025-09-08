students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

print(
    'Список пар "ID студента — возраст":',
    [
        (i, students[i]['age'])
        for i in students
        if 'age' in students[i]
    ]
)

print(
    'Полный список интересов всех студентов:',
    {
        k
        for i, j in students.items()
        if 'interests' in j
        for k in j['interests']
    }
)

print(
    'Общая длина всех фамилий студентов:',
    sum(
        [
            len(students[i]['surname'])
            for i in students
            if 'surname' in students[i]
        ]
    )
)
