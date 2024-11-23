class BalancedBrackets:
    def clear_expr(expression):
        brackets = ['(', ')', '[', ']', '{', '}']
        cleared_expr = ''
        for char in expression:
            if char in brackets:
                cleared_expr += char
        return cleared_expr