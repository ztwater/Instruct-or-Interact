class ExpressionCalculator:
    def is_operator(char):
        operators = {'+', '-', '*', '/', '(', ')', '%'}
        return char in operators