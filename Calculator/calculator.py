from polish_notation import ExpressionEvaluator

evaluator = ExpressionEvaluator()
infix_expression = input("Enter your expression: ")
postfix_expression = evaluator.postfix_expression(infix_expression)
print("Postfix expression:", postfix_expression)
result = evaluator.compile_calculate(postfix_expression)
print("Result:", result)

