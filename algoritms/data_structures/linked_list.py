class Node:
    """Узел связного списка"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Односвязный список"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Добавление элемента в конец списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        next_object = self.head
        if next_object.next is None:
            next_object.next = new_node
        else:
            while next_object.next:
                next_object = next_object.next
            next_object.next = new_node

    def prepend(self, data):
        """Добавление элемента в начало списка"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node



    def delete(self, data):
        """Удаление первого найденного элемента с data"""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next


    def search(self, data):
        """Поиск элемента, возвращает True если найден"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Вывод списка в виде [data1 -> data2 -> ...]"""
        current = self.head
        linked_list_str = ""
        while current:
            linked_list_str += f"{current.data}->"
            current = current.next
        linked_list_str += "None"
        return linked_list_str


    def get_first(self):
        """Метод для получения данных головы"""
        if not self.head:
            return None
        return self.head.data


    def remove_first(self):
        """Метод для удаления головы"""
        if not self.head:
            raise IndexError("Cannot remove from empty list")

        data = self.head.data
        self.head = self.head.next
        return data


    def get_size(self):
        """Метод для получения размера"""
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter


    @property
    def is_empty(self):
        """Свойство для проверки на пустоту"""
        return self.head is None


ll = LinkedList()

# Тест 1: Удаление из пустого списка
ll.delete(1)  # не должно быть ошибки
print(f"Пустой: {ll.display()}")  # None

# Тест 2: Добавляем и удаляем
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)  # дубликат
print(f"До удаления: {ll.display()}")  # 1->2->3->2->None

# Тест 3: Удаление из середины
ll.delete(2)
print(f"После удаления первой 2: {ll.display()}")  # 1->3->2->None

# Тест 4: Удаление головы
ll.delete(1)
print(f"После удаления головы: {ll.display()}")  # 3->2->None

# Тест 5: Удаление последнего
ll.delete(2)
print(f"После удаления последнего: {ll.display()}")  # 3->None

# Тест 6: Удаление единственного
ll.delete(3)
print(f"После удаления единственного: {ll.display()}")  # None