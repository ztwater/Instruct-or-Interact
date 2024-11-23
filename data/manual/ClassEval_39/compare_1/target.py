class ExpressionCalculator:
    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 3
        }
        
        if self.operat_priority[precedence.get(cur, 0)] >= self.operat_priority[precedence.get(peek, 0)]:
            return True
        else:
            return False