import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: float | int = 0) -> float | int:
        return radius * 2 * math.pi

    @classmethod
    def circle_sq(cls, radius: float | int = 0) -> float | int:
        return radius ** 2 * math.pi

    @classmethod
    def v_cube(cls, edge: float | int = 0) -> float | int:
        return edge ** 3

    @classmethod
    def s_sphere(cls, radius: float | int = 0) -> float | int:
        return radius ** 2 * math.pi * 4


data_1, data_2, data_3, data_4, = 5, 6, 10, 6
res_1 = MyMath.circle_len(radius=data_1)
res_2 = MyMath.circle_sq(radius=data_2)
res_3 = MyMath.v_cube(edge=data_3)
res_4 = MyMath.s_sphere(radius=data_4)
print(f'Длина окружности с радиусом {data_1} равна {res_1}')
print(f'Площадь окружности с радиусом {data_2} равна {res_2}')
print(f'Объем куба с ребром {data_3} равна {res_3}')
print(f'Площадь поверхности сферы с радиусом {data_4} равна {res_4}')
