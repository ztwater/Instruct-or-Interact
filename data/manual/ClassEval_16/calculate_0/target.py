class Calculator:
    def calculate(self, expression):
        operand_stack = []
        operator_stack = []
    
        # Function to get the precedence of an operator
        def precedence(operator):
            if operator == '^':
                return 3
            elif operator in ['*', '/']:
                return 2
            elif operator in ['+', '-']:
                return 1
            else:
                return 0
    
        # Function to apply the operator on top of the operator stack
        def apply_operator(operand_stack, operator_stack):
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = self.operators[operator](operand1, operand2)
            operand_stack.append(result)
    
        for char in expression:
            if char.isdigit():
                operand_stack.append(float(char))
            elif char in self.operators.keys():
                while (len(operator_stack) > 0 and precedence(char) <= precedence(operator_stack[-1])):
                    apply_operator(operand_stack, operator_stack)
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack[-1] != '(':
                    apply_operator(operand_stack, operator_stack)
                operator_stack.pop()
    
        while len(operator_stack) > 0:
            apply_operator(operand_stack, operator_stack)
    
        return operand_stack[-1] if len(operand_stack) > 0 else None