class ExpressionCalculator:
    def calculate(expression):
        stack = []
        operators = {'+': lambda a, b: a + b,
                     '-': lambda a, b: a - b,
                     '*': lambda a, b: a * b,
                     '/': lambda a, b: a / b}
    
        for token in expression:
            if token.isdigit():
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[token](operand1, operand2)
                stack.append(result)
    
        return stack.pop()