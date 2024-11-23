class TwentyFourPointGame:
    def evaluate_expression(self):
        result = eval("".join(map(str, self.nums)))
        if result == 24:
            return True
        else:
            return False