import functools
from typing import Callable


def check_permission(user_p: str) -> Callable:
    def decor_f(func: Callable) -> Callable:
        @functools.wraps(func)
        def decor_use(*args, **kwargs) -> Callable:
            try:
                if user_p in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError as p_er:
                print(f'{type(p_er).__name__}'
                      f': У пользователя недостаточно прав, чтобы выполнить функцию '
                      f'{func.__name__}')
        return decor_use
    return decor_f


user_permissions = ['admin']


@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


delete_site()
add_comment()
