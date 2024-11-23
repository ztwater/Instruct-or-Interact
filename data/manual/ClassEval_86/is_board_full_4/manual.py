### Method Description:
    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """

### Solution Code:
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

### Source Code:
    def is_board_full(board):
        for row in board:
            for cell in row:
                if cell == "":
                    return False
        return True

### Predicted Code:
    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

### Adaptation:
Total number: 5
### Raw Output:
```
    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
```

### Test Code:
class TicTacToeTestIsBoardFull(unittest.TestCase):
    # not full
    def test_is_board_full_1(self):
        ttt = TicTacToe()
        self.assertFalse(ttt.is_board_full())

    # full
    def test_is_board_full_2(self):
        ttt = TicTacToe()
        moves = [(1, 1), (0, 2), (2, 2), (0, 0), (0, 1), (2, 1), (1, 0), (1, 2), (2, 0)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertTrue(ttt.is_board_full())

    def test_is_board_full_3(self):
        ttt = TicTacToe()
        moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertFalse(ttt.is_board_full())

    def test_is_board_full_4(self):
        ttt = TicTacToe()
        moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (0, 2), (1, 2), (2, 1), (2, 2)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertTrue(ttt.is_board_full())

    def test_is_board_full_5(self):
        ttt = TicTacToe()
        moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (0, 2), (1, 2), (2, 1)]
        for move in moves:
            ttt.make_move(move[0], move[1])
        self.assertFalse(ttt.is_board_full())

### Test Output:
# 0 errors, 3 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_is_board_full_1: True is not false
#         test_is_board_full_3: True is not false
#         test_is_board_full_5: True is not false


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.board
# method_dependencies: 


