def input_number():
    return int(input('input number: '))

def input_operation():
   return input('operation: ')

def is_valid_operation(operation, list_operations: dict):
    return operation in list_operations.keys()

def calc(number_1, operation, number_2):
    result = None

    if operation == '-':
        result = number_1 - number_2
    if operation == '+':
        result = number_1 + number_2
    if operation == '*':
        result = number_1 * number_2
    if operation == '/':
        result = number_1 / number_2
    return result

def process(number_1, operation, number_2, available_operations):
    if is_valid_operation(operation, available_operations):
        result = calc(number_1, available_operations[operation], number_2)
    else:
        result = 'не допустимая операция'
    return result


available_operations = {
    '-' : '-',
    '+' : '+',
    '*' : '*',
    '/' : '/'
}

http_available_operations = {
    'sub': '-',
    'add': '+',
    'mul': '*',
    'div': '/'
}



if __name__ == '__main__':
    number_1 = input_number()
    while True:
        operation = input_operation()

        if is_valid_operation(operation, available_operations):
            number_2 = input_number()
            result = calc(number_1, operation, number_2)
            number_1 = result
        else:
            result = 'не допустимая операция'
        print(result)
