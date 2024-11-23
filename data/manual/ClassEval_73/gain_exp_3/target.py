class RPGCharacter:
    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next level up until exhausted
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        while self.exp >= self.level * 100:
            self.exp -= self.level * 100
            self.level += 1
            self.level_up()
        return self.exp, self.level