class RPGCharacter:
    def heal(character):
        character['hp'] += 10
        if character['hp'] > 100:
            character['hp'] = 100