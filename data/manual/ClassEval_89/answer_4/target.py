class TwentyFourPointGame:
    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
        # Base case: if there is only one card left, check if its value is 24
        if len(self.nums) == 1:
            return self.nums[0] == 24
    
        # Iterate through all possible pairs of cards
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                a = self.nums[i]
                b = self.nums[j]
    
                # Generate all possible results from combining the two cards
                results = [a + b, a - b, b - a, a * b]
                if b != 0:
                    results.append(a / b)
                if a != 0:
                    results.append(b / a)
    
                # Recursively check if any of the results can evaluate to 24
                for result in results:
                    # Remove the used cards and add the result to the remaining cards
                    remaining_cards = [self.nums[k] for k in range(len(self.nums)) if k != i and k != j]
                    remaining_cards.append(result)
    
                    # Recursively check if the remaining cards can evaluate to 24
                    if self.answer(remaining_cards):
                        return True
    
        # If no combination evaluates to 24, return False
        return False