from random import randint

"""
Игра Жизнь (Конвея)
1. есть плоскость 10x10
2. ячейки могут нходиться в состоянии жив-мертв
3. случайным образом заполняем таблицу живыми ячейками
4. на каждой итерации проверям живая или мертвая яцейка
правила таковы:
- если 0 или 1 сосед клетка умирает
- если у метвой клетки 3 соседа клетка оживает
- если у живой клетки два или три соседа она продолжает жить
- если у живой клетки больше 3-х соседей она умирает

5. создать классы для игры пригодные для использования с веб запросами

field= []
clone = field.copy()
for x in range(0, size):
    for  y in range(0, size):
        cell = field[x][y]
        change = check_cell_change()
        clone[x][y] = change
field = clone
"""

class Position:
    def __init__(self, x:int, y:int) -> None:
        self.x =x
        self.y =y


def print_field(field):
    for val in field:
        print(' '.join(val))


def init(x, y):
    return [[DEAD if randint(0, 1) == 0 else LIFE for i in range(x)] for j in range(y)]


def neighbors_count(field, position: Position):
    neighbors = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = position.x + dx
            ny = position.y + dy
            if nx < 0 or ny < 0:
                neighbors += 1
                continue
            if nx > (WIDTH - 1) or ny > (HIEGHT - 1):
                neighbors += 1
                continue
            neighbors += 1 if field[nx][ny] == LIFE else 0
    return neighbors


def life_or_dead(clone_field, field, neighbors, position: Position):
    if neighbors <= 1:
        clone_field[position.x][position.y] = DEAD
    if neighbors == 2:
        clone_field[position.x][position.y] = field[position.x][position.y]
    if neighbors == 3:
        clone_field[position.x][position.y] = LIFE
    if neighbors > 3:
        clone_field[position.x][position.y] = DEAD
    return clone_field

LIFE = 'X'
DEAD = ' '
WIDTH = 10
HIEGHT = 10

def game(field):
    while True:
        print_field(field)
        input('next step?')

        clone_field = init(WIDTH, HIEGHT)
        for y in range(HIEGHT):
            for x in range(WIDTH):
                position = Position(x, y)
                neighbors = neighbors_count(field, position)
                clone_field = life_or_dead(clone_field, field,neighbors, position)
        field = clone_field.copy() 

if __name__ == '__main__':
    field = init(WIDTH, HIEGHT)
    game(field)