array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


def answer_1(): return [x for x in array_1 if x in array_2 and x in array_3]


def answer_2(): return set(array_1).intersection(set(array_2)).intersection(set(array_3))


def answer_3(): return [x for x in array_1 if x not in array_2 and x not in array_3]


def answer_4(): return set(array_1).difference(set(array_2)).difference(set(array_3))


print('Задача 1:')
print('\tРешение без множеств:', answer_1())
print('\tРешение с множествами:', answer_2())
print('Задача 2:')
print('\tРешение без множеств:', answer_3())
print('\tРешение с множествами:', answer_4())
