class Calculator:
    def apply_operator(operator_stack, number_stack):
        operator = operator_stack.pop()
        num2 = number_stack.pop()
        num1 = number_stack.pop()
    
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")
    
        number_stack.append(result)