from Calculator.Stack.stack import Stack

# TODO: print all numbers
expression = [2, '*', 2, '+', 2, '/', 3, '-', 4]

# def print_all_numbers(arg):
#     for i in arg:
#         if type(i) == int or type(i) == float:
#             print(i)

# print_all_numbers(expression)

# TODO: pull all numbers in Stack

PRIORITIES = {
    '^': 3,
    '*': 2,
    '/': 2,        
    "+": 1,
    "-": 1,
}

stack = Stack()
operand_stack = Stack()
for i in expression:
    if type(i) == int or type(i) == float:
        stack.push(i)
    elif i == '+' or i == '-' or i == '*' or i == '/':
        # TODO make it work
        value = operand_stack.pop()
        if value is None:
            operand_stack.push(i)
        elif PRIORITIES[i] > PRIORITIES[value]:
            operand_stack.push(value)
            operand_stack.push(i)
        else:
            operand_stack.push(i)
            operand_stack.push(value)


while True:
    value = stack.pop()
    if value == None:
        break
    print(value)

while True:
    value = operand_stack.pop()
    if value == None:
        break
    print(value)