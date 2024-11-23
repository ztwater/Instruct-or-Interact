class Calculator:
    def precedence(operator):
        if operator == '^':
            return 3
        elif operator == '/' or operator == '*':
            return 2
        elif operator == '+' or operator == '-':
            return 1
        else:
            return 0