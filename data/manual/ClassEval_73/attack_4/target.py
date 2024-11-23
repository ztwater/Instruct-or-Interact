class RPGCharacter:
    def attack(self, other_character):
        damage_caused = self.attack_power - other_character.defense
        other_character.hp -= damage_caused