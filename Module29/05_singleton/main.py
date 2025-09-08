from typing import Callable
import functools


def singleton(cls: Callable) -> Callable:
    @functools.wraps(cls)
    def decor(*args, **kwargs) -> Callable:
        result = cls(*args, **kwargs)
        if hasattr(cls, 'object_singleton'):
            return cls.object_singleton
        else:
            cls.object_singleton = result
            return result
    return decor


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
