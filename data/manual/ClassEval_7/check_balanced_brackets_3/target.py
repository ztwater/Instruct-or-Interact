class BalancedBrackets:
    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)
            elif char in self.right_brackets:
                if not self.stack:
                    return False
                if self.left_brackets.index(self.stack.pop()) != self.right_brackets.index(char):
                    return False
        return len(self.stack) == 0