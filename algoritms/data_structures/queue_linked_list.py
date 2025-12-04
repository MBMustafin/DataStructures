from logging import raiseExceptions

from algoritms.data_structures.node import Node

class QueueLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, item):
        """Добавить элемент в конец очереди"""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self._size += 1
        return

    def dequeue(self):
        """Удалить и вернуть элемент из начала очереди"""
        if self.head is None:
            raise IndexError("Head of queue doesn't exist")
        else:
            answer = self.head.data
            self.head = self.head.next
            self._size -= 1
            if self.head is None:
                self.tail = None
        return answer


    def front(self):
        """Посмотреть первый элемент (без удаления)"""
        if self.head is None:
            raise IndexError("Head of queue doesn't exist")
        return self.head.data

    def is_empty(self):
        """Проверка на пустоту"""
        return self.head is None

    def size(self):
        """Количество элементов"""
        return self._size

    def __str__(self):
        """Строковое представление (от начала к концу)"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Queue([" + ", ".join(elements) + "])"