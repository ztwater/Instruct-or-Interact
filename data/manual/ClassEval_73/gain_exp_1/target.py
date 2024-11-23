class RPGCharacter:
    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next level up untill exhausts
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        exp_needed = self.level * 100
        while self.exp >= exp_needed:
            self.level += 1
            self.exp -= exp_needed
            exp_needed = self.level * 100
        return None