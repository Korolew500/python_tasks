import time


class LRUCache:
    def __init__(self, len_cache: int = 5) -> None:
        self.len_cache = len_cache
        self._cache = {}

    @property
    def cache(self):
        if len(self._cache) > 0:
            count_time, count_key = time.time(), ''
            for i_key, i_value in self._cache.items():
                if count_time > i_value[1]:
                    count_time = i_value[1]
                    count_key = i_key
            self._cache[count_key][1] = time.time()
            time.sleep(0.001)
            return self._cache[count_key][0]
        else:
            return None

    @cache.setter
    def cache(self, cash_tuple: tuple) -> None:
        key_cache = cash_tuple[0]
        value_cache = cash_tuple[1]
        self._cache[key_cache] = [value_cache, time.time()]
        time.sleep(0.001)
        if len(self._cache) > self.len_cache:
            count_time, count_key = time.time(), ''
            for i_key, i_value in self._cache.items():
                if count_time > i_value[1]:
                    count_time = i_value[1]
                    count_key = i_key
            self._cache.pop(count_key)

    def print_cache(self) -> None:
        count = len(self._cache)
        for i_key, i_value in self._cache.items():
            if count > 1:
                print(f'{i_key} : {i_value[0]}, ', end='')
            else:
                print(f'{i_key} : {i_value[0]}')
            count -= 1

    def get(self, name_key: str = None) -> str:
        if name_key in self._cache:
            self._cache[name_key][1] = time.time()
            time.sleep(0.001)
        return self._cache.get(name_key)[0]


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ('key1', 'value1')
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
