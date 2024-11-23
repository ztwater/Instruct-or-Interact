class TwentyFourPointGame:
    def evaluate_expression(self, expression):
        result = eval(expression)
        if result == 24:
            return True
        else:
            return False