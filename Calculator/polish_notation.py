class ExpressionEvaluator:
    
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def _add_spaces(self, expression):
        result = ""
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                digits = []
                digits.append(expression[i])
                i += 1
                while i < len(expression) and expression[i].isdigit():
                    digits.append(expression[i])
                    i += 1
                result += "".join(digits) + " "
            else:
                result += expression[i] + " "
                i += 1
        return result
    
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
    
    def compile_calculate(self, expression):
        try:
            spaces_expression = self._add_spaces(expression)
            postfix_expression = self._infix_to_postfix(spaces_expression)
            result = self._calculate(postfix_expression)
            return result
        except Exception as error:
            print("Ошибка ввода: ", error)
    
    def postfix_expression(self, expression):
        try:
            spaces_expression = self._add_spaces(expression)
            print(spaces_expression)
            infix_expression = self._infix_to_postfix(spaces_expression)
            return infix_expression
        except Exception as error:
            print("Ошибка ввода: ", error)