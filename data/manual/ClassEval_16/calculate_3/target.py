class Calculator:
    def calculate(self, expression):
        operand_stack = []
        operator_stack = []

        for char in expression:
            if char.isdigit():
                operand_stack.append(int(char))
            elif char in self.operators:
                while operator_stack and self.precedence(char) <= self.precedence(operator_stack[-1]):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack[-1] != '(':
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.pop()

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None