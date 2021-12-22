"""
Этап 1

1. Создать класс для игрового объекта,
свойства класс
- имя
- здоровье
- урон

методы класс:
- инициализация
- ударить
- жив_или_мертв
- лечиться

2. Класс Игра
свойства класса
- персонаж 1
- персонаж 2
методы класса:
- ход
    случайным образом выбирается действия для персонажа бить или лечиться
- вывести состояние персонажей

3. написать юниттесты для этих классов


Игровые объекты неподвижные
4. Добавить игровые объекты:
гора(нельзя испльзовать, нельзя пройти),
дерево(можно использовать, нельзя пройти),
зелье(можно испоьзовать, можно пройти),
ручей(нельзя использовать, можно пройти)

Персонажи могут ходить, бегать, кушать
5. Добавить персонажей:
волк(может кусать),
человек(может рубить, хилиться, защищаться, может носить экипировку),
орк(может рубить, хилиться, защищаться, может носить экипировку),
оборотень(может кусать, может хилиться)

"""

from random import randint
from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, capability: list):
        self.capability = capability

class Features:
    def __init__(self, hp, strenght, agility, intellect):
        self.intellect = intellect
        self.agility = agility
        self.strenght = strenght
        self.hp = hp

class Alive(Object):
    def __init__(self, name: str, features: Features, capability: list):
        super().__init__(capability)
        self.name = name
        self.default_features = features
        self.current_features = features


class Lifeless(Object):
    def __init__(self, name: str, capability: list):
        super().__init__(capability)
        self.name = name


class Action(ABC):
    @abstractmethod
    def action(self, obj: Object):
        pass

class Cut(Action):
    def action(self, obj:Object):
        pass


class Bite(Action):
    def action(self, obj:Object):
        pass


class Def(Action):
    def action(self, obj:Object):
        pass


class Heal(Action):
    def action(self, obj:Object):
        pass


class WearArmor(Action):
    def action(self, obj:Object):
        pass


class Mountains(Lifeless):
    pass

class Tree(Lifeless):
    pass

class Potion(Lifeless):
    pass


class River(Lifeless):
    pass

class Wolf(Alive):
    pass


class Human(Alive):
    pass


class Orc(Alive):
    pass


class Werewolf(Alive):
    pass



class PlayerState:
    def __init__(self, name, life):
        self.life = life
        self.name = name


class Player:
    def __init__(self, name, life: int, damage: int, heal: int):
        self.name = name
        self.life = life
        self.max_life = life
        self.damage = damage
        self.heal = heal

    def is_dead(self):
        return self.life <= 0

    def healing(self):
        self.life = min(self.life + self.heal, self.max_life)

    def kick(self, enemy):
        enemy.hit(self.damage)

    def hit(self, damage):
        self.life -= damage

    def state(self) -> PlayerState:
        return PlayerState(self.name, self.life)


# 2
class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two

    def step(self):
        self.action(self.what_do(), self.player_one, self.player_two)
        self.action(self.what_do(), self.player_two, self.player_one)

    def what_do(self):
        return randint(0, 1)

    def is_end(self):
        return self.player_one.is_dead() or self.player_two.is_dead()

    def winner(self):
        return self.player_one.name if self.player_two.is_dead() else self.player_two.name

    def state(self):
        return (
            self.player_one.state(),
            self.player_two.state()
        )

    def action(self, action, player: Player, enemy: Player):
        if action == 0:
            player.kick(enemy)
        if action == 1:
            player.healing()


if __name__ == '__main__':
    game = Game(Player('Human', 100, 20, 10), Player('Ork', 200, 10, 1))
    while not game.is_end():
        for player_info in game.state():
            print(f"Player {player_info.name} life {player_info.life}")
        game.step()
    else:
        print(f"winner {game.winner()}")
