class ExpressionEvaluator:
    
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    def _infix_to_postfix(self, expression):
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
    
    def _calculate(self, expression):
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
                elif token == '^':
                    stack.append(num1 ** num2)
        return stack[0]
    
    def evaluate_expression(self, expression):
        postfix_expression = self._infix_to_postfix(expression)
        result = self._calculate(postfix_expression)
        return result
    
    def compile_calculate(self, expression):
        postfix_expression = self._infix_to_postfix(expression)
        result = self._calculate(postfix_expression)
        return result
    
    def evaluate_expression(self, expression):
        result = self.compile_calculate(expression)
        return result
