class RPGCharacter:
    def gain_exp(exp, level):
        exp_needed = level * 100
        if exp >= exp_needed:
            level += 1
            print("Level up!")
        else:
            print("No level up yet.")
        return level