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
        Level up the character and return the new level, health points, attack power, and defense points.
        """
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
        self.exp = 0
        
        return self.level, self.hp, self.attack_power, self.defense

### Adaptation:
Total number: 29
### Raw Output:
To adapt the `level_up` method to the `RPGCharacter` class, you can modify the provided method as follows:

```python
def level_up(self):
        """
        Level up the character and return the new level, health points, attack power, and defense points.
        """
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
        self.exp = 0
        
        return self.level, self.hp, self.attack_power, self.defense
```

You need to remove the `global` statement and change the variable names to use the instance variables (`self.hp`, `self.attack_power`, `self.defense`, and `self.exp`) instead of the global variables (`hp`, `attack_power`, `defense_points`, and `experience_points`). Finally, return the new level, health points, attack power, and defense points as a tuple.

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
# 0 errors, 5 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_level_up_1: 1 != 2
#         test_level_up_2: 120 != 100
#         test_level_up_3: 2 != 3
#         test_level_up_4: 3 != 4
#         test_level_up_5: 4 != 5


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.attack_power, self.defense, self.exp, self.hp, self.level
# method_dependencies: attack


