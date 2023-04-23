from polish_notation import ExpressionEvaluator

evaluator = ExpressionEvaluator()
infix_expression = input("Enter your expression: ")
postfix_expression = evaluator.infix_to_postfix(infix_expression)
print("Postfix expression:", postfix_expression)
result = evaluator.calculate(postfix_expression)
print("Result:", result)
result = evaluator.evaluate_expression(infix_expression)
print("Result from infix expression:", result)
