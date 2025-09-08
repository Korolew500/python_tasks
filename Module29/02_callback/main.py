import functools
from collections.abc import Callable
from typing import Optional


def callback(cb: str) -> Callable:
    def all_decor(func: Callable) -> Callable:
        @functools.wraps(func)
        def decor(*args, **kwargs) -> Optional[Callable]:
            function = func(*args, **kwargs)
            if cb in args or cb in kwargs.values():
                return function
            else:
                return None
        return decor
    return all_decor


class App:
    def __init__(self):
        self.body = []

    @callback('//')
    def get(self, sign: str) -> str:
        self.body.append(sign)
        print('Пример функции, которая возвращает ответ сервера')
        return 'OK'


app = App()

route = app.get('//')  # OK
if route:
    response = route
    print('Ответ:', response)
else:
    print('Такого пути нет')

print()

route = app.get('С://')  # Такого пути нет
if route:
    response = route
    print('Ответ:', response)
else:
    print('Такого пути нет')
