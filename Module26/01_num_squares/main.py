class Cubs:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.count = 0
        self.cubs = [str((cub + 1) ** 2) for cub in range(self.limit)]

    def __iter__(self) -> iter:
        self.count = 0
        return self

    def __next__(self) -> str:
        self.count += 1
        if self.count <= self.limit:
            return self.cubs[self.count - 1]
        else:
            raise StopIteration


def cubs_f(number: int) -> str:
    for i_num in range(number):
        yield str((i_num + 1) ** 2)


user_number = int(input('Введите целое число: '))
class_list = Cubs(user_number)
generator_list = cubs_f(user_number)
srt_list = [str((cub + 1) ** 2) for cub in range(user_number)]

print('Результат работы итерируемого класса:    ', ', '.join(class_list))
print('Результат работы генераторной функции:   ', ', '.join(generator_list))
print('Результат работы генераторного выражения:', ', '.join(srt_list))
