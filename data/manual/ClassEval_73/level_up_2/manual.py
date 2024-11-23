### Method Description:
    def level_up(self):
         """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """

### Solution Code:
    def level_up(self):
        if self.level < 100:
            self.level += 1
            self.exp = 0
            self.hp += 20
            self.attack_power += 5
            self.defense += 5
        return self.level, self.hp, self.attack_power, self.defense

### Source Code:
    def level_up():
        global hp, attack_power, defense_points, experience_points
        
        hp += 20
        attack_power += 5
        defense_points += 5
        experience_points = 0
        
        return hp, attack_power, defense_points

### Predicted Code:
    def level_up(self):
        """
        Level up the character and return the new level, health points, attack power, and defense points after leveling up.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        """
        self.level += 1
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
        self.exp = 0

        return self.level, self.hp, self.attack_power, self.defense

### Adaptation:
Total number: 40
### Raw Output:
```python
class RPGCharacter:  
    """
    The class represents a role-playing game character, which allows to attack other characters, heal, gain experience, level up, and check if the character is alive.
    """

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        :param name: strm, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0


    def attack(self, other_character):
        pass

    def heal(self):
        pass

    def gain_exp(self, amount):
        pass

    def is_alive(self):
        pass

    def level_up(self):
        """
        Level up the character and return the new level, health points, attack power, and defense points after leveling up.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        """
        self.level += 1
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
        self.exp = 0

        return self.level, self.hp, self.attack_power, self.defense
```

### Test Code:
class RPGCharacterTestLevelUp(unittest.TestCase):
    def test_level_up_1(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.level_up()
        self.assertEqual(character.level, 2)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 25)
        self.assertEqual(character.defense, 15)

    # full level
    def test_level_up_2(self):
        character = RPGCharacter("John", 100, 20, 10, 100)
        character.level_up()
        self.assertEqual(character.level, 100)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 100)
        self.assertEqual(character.attack_power, 20)
        self.assertEqual(character.defense, 10)

    def test_level_up_3(self):
        character = RPGCharacter("John", 100, 20, 10, 2)
        character.level_up()
        self.assertEqual(character.level, 3)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 25)
        self.assertEqual(character.defense, 15)

    def test_level_up_4(self):
        character = RPGCharacter("John", 100, 20, 10, 3)
        character.level_up()
        self.assertEqual(character.level, 4)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 25)
        self.assertEqual(character.defense, 15)

    def test_level_up_5(self):
        character = RPGCharacter("John", 100, 20, 10, 4)
        character.level_up()
        self.assertEqual(character.level, 5)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 25)
        self.assertEqual(character.defense, 15)

### Test Output:
# 0 errors, 1 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_level_up_2: 101 != 100


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.attack_power, self.defense, self.exp, self.hp, self.level
# method_dependencies: attack


