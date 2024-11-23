class RPGCharacter:
    def gain_exp(self, amount):
        """
        Gain experience points for the character and level up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next level up until exhausted
        :param amount: int, the amount of experience points to gain.
        """
        current_exp_needed = self.level * 100
        self.exp += amount
        while self.exp >= current_exp_needed:
            self.exp -= current_exp_needed
            self.level += 1
            current_exp_needed = self.level * 100
            print("Level up!")