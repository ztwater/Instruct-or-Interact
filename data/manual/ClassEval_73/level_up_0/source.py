class RPGCharacter:
    def level_up():
        global hp, attack_power, defense_points, experience_points
        
        hp += 20
        attack_power += 5
        defense_points += 5
        experience_points = 0
        
        return hp, attack_power, defense_points