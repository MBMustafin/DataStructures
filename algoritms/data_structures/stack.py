from algoritms.data_structures.linked_list import LinkedList

class Stack:
    def __init__(self):
        """Инициализация пустого стека"""
        self.items = []


    def push(self, item):
        """Добавить элемент на вершину стека"""
        self.items.append(item)

    def pop(self):
        """
        Удалить и вернуть элемент с вершины стека.

        Raises:
            IndexError: если стек пустой
        """

        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("Pop from empty stack")


    def peek(self):
        """
        Вернуть элемент с вершины стека (без удаления).

        Raises:
            IndexError: если стек пустой
        """
        try:
            return self.items[-1]
        except IndexError:
            raise IndexError("Peak from empty stack")

    def is_empty(self) -> bool:
        """Проверка, пуст ли стек"""
        return len(self.items) == 0


    def size(self) -> int:
        """Количество элементов в стеке"""
        return len(self.items)

    def __str__(self):
        """Строковое представление стека"""
        return f"Stack({self.items})"

    def __len__(self) -> int:
        """Поддержка len(stack)"""
        return self.size()