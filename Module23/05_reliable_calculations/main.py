import math


def get_sage_sqrt(num):
    try:
        if not (isinstance(num, int) or isinstance(num, float)):
            raise TypeError
        elif num < 0:
            raise ValueError
        else:
            return round(math.sqrt(num), 2)
    except TypeError:
        return 'Ошибка, это не число.'
    except ValueError:
        return 'Ошибка, невозможно вычислить квадратный корень из отрицательного числа.'
    except Exception as exc:
        return exc


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
