class ExpressionCalculator:
    def calculate(self, expression):
        stack = []
        operators = {'+': lambda a, b: a + b,
                     '-': lambda a, b: a - b,
                     '*': lambda a, b: a * b,
                     '/': lambda a, b: a / b}
    
        for token in expression:
            if token.isdigit():
                stack.append(int(token))
            elif token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[token](operand1, operand2)
                stack.append(result)
    
        return stack.pop()