from typing import Any, Optional


class Node:
    """Класс узел односвязного списка"""
    def __init__(self, meaning: Optional[Any] = None, next_node: Optional['Node'] = None) -> None:
        """Создание узла:
        meaning задаёт значение, которое хранит узел,
        next_node задаёт ссылку на следующий узел"""
        self.next_node = next_node
        self.meaning = meaning

    def __str__(self) -> str:
        """Магический метод узла односвязного списка,
        который возвращает строкой значение узла meaning"""
        return str(self.meaning)

    def append(self, meaning: Optional[Any] = None) -> None:
        """Метод добавления ссылки next_node на следующий узел.
        Если ссылка на следующий узел пуста - создается новая,
        если ссылка есть, данные рекурсивно передаются дальше,
        meaning - передаваемое значение в новый узел"""
        if not self.next_node:
            self.next_node = Node(meaning)
        else:
            self.next_node.append(meaning)

    def get(self, linked_list: Optional[list] = None) -> list:
        """Метод рекурсивного чтения значений всего односвязного списка
        Изначально на входе параметров нет, лист появляется в рекурсии сам"""
        if not linked_list:
            """Создание пустого листа, если он не передан"""
            linked_list = []
        if not self.next_node:
            """Если это крайний узел односвязного списка,
            Добавляем значение узла в лист и возвращаем лист"""
            linked_list.append(self.meaning)
            return linked_list
        else:
            """Если есть ссылка на следующий узел, 
            добавляем значение текущего узла в лист,
            затем передаем лист рекурсивно в следующий узел.
            В итоге возвращаем лист со всеми значениями"""
            linked_list.append(self.meaning)
            return self.next_node.get(linked_list)


class LinkedList:
    """Класс односвязный список, в котором каждый узел это класс Node"""
    def __init__(self) -> None:
        """Создание односвязного списка.
        Переменная head изначально пуста, в ней будет ссылка на первый узел
        Переменная len содержит длину односвязного списка"""
        self.head: Optional[Node] = None
        self.len = 0

    def append(self, meaning: Optional[Any]) -> None:
        """Метод добавления узла в конец односвязного списка.
        Если головная ссылка пуста, то создается первый узел со значением meaning
        Иначе вызывается рекурсивный метод append для добавления узла в самый конец списка.
        В итоге длина списка увеличивается на 1"""
        if not self.head:
            self.head = Node(meaning)
        else:
            self.head.append(meaning)
        self.len += 1

    def __str__(self) -> str:
        """Метод вывода всего односвязного списка"""
        if self.head:
            return str(self.head.get())
        else:
            return 'None'

    def get(self, index: int) -> str:
        """Метод вывода одной позиции из односвязного списка"""
        if self.head:
            all_list = self.head.get()
            return str(all_list[index])
        else:
            return 'None'

    def remove(self, index: int) -> None:
        """Переменная cur_node это текущий узел
        cur_index это текущий индекс узла
        Здесь идет проверка на адекватность входных данных"""
        cur_node = self.head
        cur_index = 0
        prev: Optional[Node] = None
        if self.len == 0 or self.len <= index:
            raise IndexError

        if cur_node:
            """Если индекс равен 0, то работаем с головным узлом
            и заменяем ссылку на первый узел ссылкой на следующий,
            уменьшаем длину списка и выходим из метода"""
            if index == 0:
                self.head = self.head.next_node
                self.len -= 1
                return

        while cur_node:
            """Цикл для углубления в односвязный список.
            Как только текущий индекс становится равен текущему индексу, углубление завершается"""
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next_node
            cur_index += 1

        """Ссылка на текущий узел заменяется ссылкой на следующий узел.
        Длина списка уменьшается. Метод завершается"""
        prev.next_node = cur_node.next_node
        self.len -= 1
        return


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
