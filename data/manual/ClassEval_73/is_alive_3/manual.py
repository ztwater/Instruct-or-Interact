### Method Description:
    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """

### Solution Code:
    def is_alive(self):
        return self.hp > 0

### Source Code:
    def is_alive(player):
        if player.health > 0:
            return True
        else:
            return False

### Predicted Code:
    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
        if self.hp > 0:
            return True
        else:
            return False

### Adaptation:
Total number: 4
### Raw Output:
```python
    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
        if self.hp > 0:
            return True
        else:
            return False
```

### Test Code:
class RPGCharacterTestIsAlive(unittest.TestCase):
    def test_is_alive_1(self):
        character = RPGCharacter("John", 100, 20, 10)
        self.assertTrue(character.is_alive())

    def test_is_alive_2(self):
        character = RPGCharacter("John", 0, 20, 10)
        self.assertFalse(character.is_alive())

    def test_is_alive_3(self):
        character = RPGCharacter("John", -10, 20, 10)
        self.assertFalse(character.is_alive())

    def test_is_alive_4(self):
        character = RPGCharacter("John", 1, 20, 10)
        self.assertTrue(character.is_alive())

    def test_is_alive_5(self):
        character = RPGCharacter("John", 10, 20, 10)
        self.assertTrue(character.is_alive())

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.hp
# method_dependencies: 


