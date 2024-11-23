class Calculator:
    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None
        """
        operand_stack = []
        operator_stack = []

        for char in expression:
            if char.isdigit():
                operand_stack.append(float(char))
            elif char in self.operators.keys():
                while operator_stack and self.precedence(char) <= self.precedence(operator_stack[-1]):
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    result = self.operators[operator](operand1, operand2)
                    operand_stack.append(result)
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    result = self.operators[operator](operand1, operand2)
                    operand_stack.append(result)
                operator_stack.pop()

        while operator_stack:
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = self.operators[operator](operand1, operand2)
            operand_stack.append(result)

        if operand_stack:
            return operand_stack.pop()
        else:
            return None
