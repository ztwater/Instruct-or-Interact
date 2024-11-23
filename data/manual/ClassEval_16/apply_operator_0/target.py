class Calculator:
    def apply_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        num2 = operand_stack.pop()
        num1 = operand_stack.pop()
        
        if operator in self.operators:
            result = self.operators[operator](num1, num2)
        else:
            raise ValueError("Invalid operator")
        
        operand_stack.append(result)
        
        return operand_stack, operator_stack