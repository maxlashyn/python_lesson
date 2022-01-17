from abc import ABC, abstractmethod
from random import randint


class Field:
    def __init__(self, width=3, height=3):
        self.height = height
        self.width = width
        self.field = self.init_field()

    def init_field(self):
        return [[" " for i in range(0, self.width)] for j in range(0, self.height)]

    def place(self, char: str, x: int, y: int):
        if self.is_empty(x, y):
            self.field[x][y] = char

    def is_empty(self, x, y):
        return self.field[x][y] == ' '


class Presenter(ABC):
    @abstractmethod
    def print(self, field: Field):
        pass


class Console(Presenter):
    def hr(self, width):
        return ['-' for i in range(0, width * 2 + 1)]

    def print(self, field: Field):
        print("".join(self.hr(field.width)))
        for y in range(0, field.height):
            print(f"|{'|'.join(field.field[y])}|")
            print("".join(self.hr(field.width)))


class Html(Presenter):
    def print(self, field: Field):
        # return render_template()
        print('from html')


class Player(ABC):
    @abstractmethod
    def turn(self, field: Field):
        pass


class Computer(Player):
    def turn(self, field: Field):
        return [randint(0, field.width), randint(0, field.height)]


class Human(Player):
    def turn(self, field: Field):
        x = int(input('x='))
        y = int(input('y='))
        return [x, y]


class Game:
    def __init__(self, presenter: Presenter):
        self.presenter = presenter
        self.field = Field()
        self.computer = Computer()
        self.human = Human()

    def print(self):
        self.presenter.print(self.field)

    def main_loop(self):
        while True:
            self.step()

    def step(self):
        self.print()
        x, y = self.computer.turn(self.field)
        self.field.place('0', x, y)
        self.print()
        x, y = self.human.turn(self.field)
        self.field.place('x', x, y)
