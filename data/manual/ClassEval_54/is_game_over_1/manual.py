### Method Description:
    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        >>> mc = MahjongConnect([4, 4] ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """

### Solution Code:
    def is_game_over(self):
        for row in self.board:
            if any(icon != ' ' for icon in row):
                return False
        return True

### Source Code:
    def is_game_over(game_board):
        for row in game_board:
            for icon in row:
                if icon != "":
                    return False
        return True

### Predicted Code:
    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        """
        for row in self.board:
            for icon in row:
                if icon != " ":
                    return False
        return True

### Adaptation:
Total number: 7
### Raw Output:
To adapt the `is_game_over` method to the `MahjongConnect` class context, you can modify the method signature to include the `self` parameter. The adapted method should iterate over the `board` attribute of the `MahjongConnect` instance and check if any icon is present. If an icon is found, the method should return `False` to indicate that the game is not over. If no icons are found, the method should return `True` to indicate that the game is over.

Here's the adapted `is_game_over` method for the `MahjongConnect` class:

```python
def is_game_over(self):
    """
    Check if the game is over (i.e., if there are no more icons on the game board)
    :return: True or False ,representing whether the game is over
    """
    for row in self.board:
        for icon in row:
            if icon != " ":
                return False
    return True
```

You can replace the existing `is_game_over` method in the `MahjongConnect` class with this adapted version.

### Test Code:
class MahjongConnectTestIsGameOver(unittest.TestCase):
    def test_is_game_over_1(self):
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [[' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ']]
        res = mc.is_game_over()
        self.assertEqual(res, True)

    def test_is_game_over_2(self):
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', ' ', ' ', ' '],
                    ['a', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ']]
        res = mc.is_game_over()
        self.assertEqual(res, False)

    def test_is_game_over_3(self):
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [[' ', ' ', ' ', ' '],
                    ['a', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ']]
        res = mc.is_game_over()
        self.assertEqual(res, False)

    def test_is_game_over_4(self):
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['1', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ']]
        res = mc.is_game_over()
        self.assertEqual(res, False)

    def test_is_game_over_5(self):
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ']]
        res = mc.is_game_over()
        self.assertEqual(res, False)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.board
# method_dependencies: 


