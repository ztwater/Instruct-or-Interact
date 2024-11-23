class RPGCharacter:
    def level_up(self):
        """
        Level up the character and return the new level, health points, attack power, and defense points.
        """
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
        self.exp = 0
        
        return self.level, self.hp, self.attack_power, self.defense