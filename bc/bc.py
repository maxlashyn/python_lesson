"""
используя click
сделать консольное приложение
которое будет
1. команда calc которая будет вычислять простое выражение
    1+2 3-2 5*6 6/2
    '1+2'.count('+') => 1
    '1+2'.split('+') => [1, 2]

2. команда check которая будет проверять
соответствие закрывающих скобок открывающим
([{}])
(5 + 6) результат "ок"
(5 + 6 результат "не хватает скобки"
5 + 6) результат "не хватает скобки"
((5+6) (* (7-2))

"""

import click
from bc.stack import Stack

@click.group('main_group')
def main_group():
    pass


# 1
@main_group.command()
@click.argument('evaluation', default='')
def calc(evaluation: str):
    from bc.calc import process, available_operations
    result = 'undefined'
    if evaluation.count('+') > 0:
        number1, number2 = evaluation.split('+')
        result = process(int(number1), '+', int(number2), available_operations)
    if evaluation.count('-') > 0:
        number1, number2 = evaluation.split('-')
        result = process(int(number1), '-', int(number2), available_operations)
    if evaluation.count('*') > 0:
        number1, number2 = evaluation.split('*')
        result = process(int(number1), '*', int(number2), available_operations)
    if evaluation.count('/') > 0:
        number1, number2 = evaluation.split('/')
        result = process(int(number1), '/', int(number2), available_operations)
    print(f"{evaluation} = {result}")


@main_group.command()
@click.argument('evaluation', default='')
def check(evaluation: str):
    stack = Stack()
    for i in evaluation:
        if i == '(':
            stack.push(i)
        if i == ')':
            if stack.size() > 0:
                a = stack.pop()
                if not a == '(':
                    stack.push(a)
            else:
                print('error')
                return
        if i == '[':
            stack.push(i)
        if i == ']':
            if stack.size() > 0:
                a = stack.pop()
                if not a == '[':
                    stack.push(a)
            else:
                print('error')
                return

    if stack.is_empty():
        print('ok')
    else:
        print('error')


if __name__ == '__main__':
    main_group()
