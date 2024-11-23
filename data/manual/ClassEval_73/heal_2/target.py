class RPGCharacter:
    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        """
        self.hp += 10
        if self.hp > 100:
            self.hp = 100