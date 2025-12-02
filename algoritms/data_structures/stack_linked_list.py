from algoritms.data_structures.linked_list import LinkedList

class StackLinkedList:

    def __init__(self):
        """Инициализация пустого стека"""
        self.items = LinkedList()

    def push(self, item):
        """Добавить элемент на вершину стека"""
        self.items.prepend(item)


    def pop(self):
        """
        Удалить и вернуть элемент с вершины стека.

        Raises:
            IndexError: если стек пустой
        """

        if self.items.is_empty:
            raise IndexError("Stack's empty")

        return self.items.remove_first()

    def peek(self):
        """Возвращает значение вершины стека
        Raises:
            IndexError: если стек пустой
        """
        if self.items.is_empty:
            raise IndexError("Stack's empty")

        return self.items.get_first()

    def is_empty(self):
        return self.items.is_empty

    def size(self):
        return self.items.get_size()

    def __str__(self):
        """Строковое представление стека"""
        if self.is_empty():
            return "StackLinkedList(empty)"

        current = self.items.head
        elem = []
        while current:
            elem.append(str(current.data))
            current = current.next
        elem.reverse()
        return "<-".join(elem)

