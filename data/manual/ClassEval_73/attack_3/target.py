class RPGCharacter:
    def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: str, The character being attacked.
        """
        damage_caused = self.attack_power - other_character.defense
        other_character.hp -= damage_caused