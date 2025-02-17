class CircularBufferList:
    def __init__(self, size):
        self.__buffer = [None] * size
        self.__size = size
        self.__start = 0
        self.__end = 0
        self.__count = 0

    def __len__(self):
        return self.__count

    def size(self):
        return self.__size

    def is_full(self):
        return self.__count == self.__size

    def is_empty(self):
        return self.__count == 0

    def __resize(self):
        new_size = self.__size * 2
        new_buffer = [None] * new_size

        for i in range(self.__count):
            new_buffer[i] = self.__buffer[(self.__start + i) % self.__size]
        self.__buffer = new_buffer
        self.__size = new_size
        self.__start = 0
        self.__end = self.__count

    def push(self, item):
        if self.is_full():
            self.__resize()

        self.__buffer[self.__end] = item
        self.__end = (self.__end + 1) % self.__size
        self.__count += 1

    def pull(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")

        item = self.__buffer[self.__start]
        self.__buffer[self.__start] = None
        self.__start = (self.__start + 1) % self.__size
        self.__count -= 1
        return item