class Stack:
    def __init__(self):
        self.__list = list()

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if self.is_empty():
            return None
        return self.__list.pop()

    def push(self, number):
        self.__list.append(number)

    def size(self):
        return len(self.__list)

    def show(self):
        print('=', self.__list)