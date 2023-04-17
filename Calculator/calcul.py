# # expression = input("Enter your expression: ")
# expression = "1+2*3"

# expression_list = []

# for value in expression:
#     if value.isdigit() or value in ['+', '-', '*', '/']:
#         expression_list.append(value)

# print(expression_list)

# result = int(expression_list[0])
# i = 1

# while i < len(expression_list):
#     if expression_list[i] == "*":
#         result *= int(expression_list[i+1])
#         i += 2

#     elif expression_list[i] == "/":
#         result /= int(expression_list[i+1])
#         i += 2


# print(result)

class ExpressionEvaluator:
    
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    def infix_to_postfix(self, expression):
        operator_stack = []
        output = []
        for token in expression.split():
            if token.isdigit():
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while operator_stack and operator_stack[-1] != '(' and self.precedence[operator_stack[-1]] >= self.precedence[token]:
                    output.append(operator_stack.pop())
                operator_stack.append(token)
        while operator_stack:
            output.append(operator_stack.pop())
        return ' '.join(output)
    
    def calculate(self, expression):
        stack = []
        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    stack.append(num1 / num2)
        return stack[0]
    
    def evaluate_expression(self, expression):
        postfix_expression = self.infix_to_postfix(expression)
        result = self.calculate(postfix_expression)
        return result

evaluator = ExpressionEvaluator()
infix_expression = input("Enter your expression: ")
postfix_expression = evaluator.infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)
result = evaluator.calculate(postfix_expression)
print("Result:", result)
result = evaluator.evaluate_expression(infix_expression)
print("Result from infix expression:", result)
