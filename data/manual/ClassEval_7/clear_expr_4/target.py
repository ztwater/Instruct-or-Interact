class BalancedBrackets:
    def clear_expr(self):
        brackets = ['(', ')', '[', ']', '{', '}']
        cleared_expr = ''
        for char in self.expr:
            if char in brackets:
                cleared_expr += char
        self.expr = cleared_expr