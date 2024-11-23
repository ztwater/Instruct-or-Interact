class ExpressionCalculator:
    def is_operator(self, c):
        operators = {'+', '-', '*', '/', '(', ')', '%'}
        return c in operators