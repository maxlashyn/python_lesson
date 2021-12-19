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
"""

from random import randint


# 1

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
