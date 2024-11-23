class RPGCharacter:
    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        """
        if self.hp > 0:
            return True
        else:
            return False