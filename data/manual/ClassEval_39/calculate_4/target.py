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
            elif self.is_operator(token):
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self._calculate(operand1, operand2, token)
                stack.append(result)
    
        return stack.pop()
