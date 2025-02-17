class Node:
    def __init__(self, value=None):
        self.value = value
        self.next: [Node | None] = None


class CircularBufferLinkedList:
    def __init__(self):
        self.__count = 0
        self.__size = 0
        self.__head: [Node | None] = None
        self.__tail: [Node | None] = None
        self.__tail_end: [Node | None] = None
        self.__is_empty = True

    def __len__(self):
        return self.__count

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__is_empty

    def push(self, item):
        self.__count += 1

        if self.is_empty():
            self.__is_empty = False

            if self.__tail is None:
                node = Node(item)
                self.__tail = node
                self.__head = node
                self.__tail_end = node
                self.__size += 1
                return

            self.__tail.value = item
            return

        node = self.__tail.next

        if node is None:
            node = Node(item)
            self.__tail.next = node
            self.__tail_end = node
            self.__size += 1
        else:
            node.value = item

        self.__tail = node

    def pull(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")

        self.__count -= 1
        item = self.__head.value

        if self.__head == self.__tail:
            self.__is_empty = True
        else:
            self.__tail_end.next = self.__head
            self.__tail_end = self.__head
            self.__head = self.__head.next

        return item
