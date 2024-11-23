class BalancedBrackets:
    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        """
        brackets = ['(', ')', '[', ']', '{', '}']
        cleared_expr = ''
        for char in self.expr:
            if char in brackets:
                cleared_expr += char
        self.expr = cleared_expr