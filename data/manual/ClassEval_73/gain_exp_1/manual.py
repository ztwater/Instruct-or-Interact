### Method Description:
    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next leve up untill exhausts
        :param amount: int, the amount of experience points to gain.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """

### Solution Code:
    def gain_exp(self, amount):
        while amount != 0:
            if self.exp + amount >= self.level * 100:
                amount -= (self.level * 100 - self.exp)
                self.level_up()
            else:
                self.exp += amount
                amount = 0

### Source Code:
    def gain_exp(exp, level):
        exp_needed = level * 100
        if exp >= exp_needed:
            level += 1
            print("Level up!")
        else:
            print("No level up yet.")
        return level

### Predicted Code:
    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next level up untill exhausts
        :param amount: int, the amount of experience points to gain.
        """
        self.exp += amount
        exp_needed = self.level * 100
        while self.exp >= exp_needed:
            self.level += 1
            self.exp -= exp_needed
            exp_needed = self.level * 100
        return None

### Adaptation:
Total number: 28
### Raw Output:
```python
def gain_exp(self, amount):
    """
    Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
    The experience that overflows should be used to calculate the next level up untill exhausts
    :param amount: int, the amount of experience points to gain.
    """
    self.exp += amount
    exp_needed = self.level * 100
    while self.exp >= exp_needed:
        self.level += 1
        self.exp -= exp_needed
        exp_needed = self.level * 100
    return None
```

### Test Code:
class RPGCharacterTestGainExp(unittest.TestCase):

    # exp not overflow
    def test_gain_exp_1(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(100)
        self.assertEqual(character.level, 2)
        self.assertEqual(character.exp, 0)

    # exp overflow
    def test_gain_exp_2(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(1100)
        self.assertEqual(character.level, 5)
        self.assertEqual(character.exp, 100)

    def test_gain_exp_3(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(200)
        self.assertEqual(character.level, 2)
        self.assertEqual(character.exp, 100)

    def test_gain_exp_4(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(300)
        self.assertEqual(character.level, 3)
        self.assertEqual(character.exp, 0)

    def test_gain_exp_5(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(400)
        self.assertEqual(character.level, 3)
        self.assertEqual(character.exp, 100)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.exp, self.level
# method_dependencies: level_up


