class ExpressionCalculator:
    def compare(operator1, operator2):
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 3
        }
        
        if precedence.get(operator1, 0) > precedence.get(operator2, 0):
            return f"{operator1} has higher precedence than {operator2}"
        elif precedence.get(operator1, 0) < precedence.get(operator2, 0):
            return f"{operator1} has lower precedence than {operator2}"
        else:
            return f"{operator1} and {operator2} have the same precedence"