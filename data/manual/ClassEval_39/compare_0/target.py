class ExpressionCalculator:
    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True
        """
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 3
        }

        cur_precedence = self.operat_priority[precedence.get(cur, 0)]
        peek_precedence = self.operat_priority[precedence.get(peek, 0)]

        if cur_precedence >= peek_precedence:
            return True
        else:
            return False