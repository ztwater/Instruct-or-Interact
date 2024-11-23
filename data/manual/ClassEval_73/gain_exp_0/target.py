class RPGCharacter:
    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next leve up untill exhausts
        :param amount: int, the amount of experience points to gain.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """
        exp_needed = self.level * 100
        self.exp += amount
        while self.exp >= exp_needed:
            self.level += 1
            self.exp -= exp_needed
            exp_needed = self.level * 100
        print("No level up yet.")