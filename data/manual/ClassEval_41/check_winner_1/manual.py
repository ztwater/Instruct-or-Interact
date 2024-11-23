### Method Description:
    def check_winner(self):
        """
        Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
        return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """

### Solution Code:
    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != ' ':
                    for direction in directions:
                        if self._check_five_in_a_row(row, col, direction):
                            return self.board[row][col]
        return None

### Source Code:
    def check_winner(board):
        # Check horizontal lines
        for row in board:
            for i in range(len(row) - 4):
                if row[i] == row[i+1] == row[i+2] == row[i+3] == row[i+4]:
                    return True
    
        # Check vertical lines
        for col in range(len(board[0])):
            for i in range(len(board) - 4):
                if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == board[i+4][col]:
                    return True
    
        # Check diagonal lines (top-left to bottom-right)
        for row in range(len(board) - 4):
            for col in range(len(board[0]) - 4):
                if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4]:
                    return True
    
        # Check diagonal lines (top-right to bottom-left)
        for row in range(len(board) - 4):
            for col in range(4, len(board[0])):
                if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == board[row+4][col-4]:
                    return True
    
        # No winner found
        return False

### Predicted Code:
    def check_winner(self):
        # Check horizontal lines
        for row in self.board:
            for i in range(len(row) - 4):
                if row[i] == row[i+1] == row[i+2] == row[i+3] == row[i+4]:
                    return self.current_player
    
        # Check vertical lines
        for col in range(len(self.board[0])):
            for i in range(len(self.board) - 4):
                if self.board[i][col] == self.board[i+1][col] == self.board[i+2][col] == self.board[i+3][col] == self.board[i+4][col]:
                    return self.current_player
    
        # Check diagonal lines (top-left to bottom-right)
        for row in range(len(self.board) - 4):
            for col in range(len(self.board[0]) - 4):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] == self.board[row+4][col+4]:
                    return self.current_player
    
        # Check diagonal lines (top-right to bottom-left)
        for row in range(len(self.board) - 4):
            for col in range(4, len(self.board[0])):
                if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] == self.board[row+4][col-4]:
                    return self.current_player
    
        # No winner found
        return None

### Adaptation:
Total number: 74
### Raw Output:
```python
    def check_winner(self):
        # Check horizontal lines
        for row in self.board:
            for i in range(len(row) - 4):
                if row[i] == row[i+1] == row[i+2] == row[i+3] == row[i+4]:
                    return self.current_player
    
        # Check vertical lines
        for col in range(len(self.board[0])):
            for i in range(len(self.board) - 4):
                if self.board[i][col] == self.board[i+1][col] == self.board[i+2][col] == self.board[i+3][col] == self.board[i+4][col]:
                    return self.current_player
    
        # Check diagonal lines (top-left to bottom-right)
        for row in range(len(self.board) - 4):
            for col in range(len(self.board[0]) - 4):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] == self.board[row+4][col+4]:
                    return self.current_player
    
        # Check diagonal lines (top-right to bottom-left)
        for row in range(len(self.board) - 4):
            for col in range(4, len(self.board[0])):
                if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] == self.board[row+4][col-4]:
                    return self.current_player
    
        # No winner found
        return None
```

### Test Code:
class GomokuGameTestCheckWinner(unittest.TestCase):
    def test_check_winner_1(self):
        gomokuGame = GomokuGame(10)
        self.assertEqual(None, gomokuGame.check_winner())

    def test_check_winner_2(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('X', gomokuGame.check_winner())

    def test_check_winner_3(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 0), (0, 4)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('O', gomokuGame.check_winner())

    def test_check_winner_4(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1), (0, 4)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual(gomokuGame.check_winner(), 'O')

    def test_check_winner_5(self):
        gomokuGame = GomokuGame(10)
        moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1), (0, 4), (5, 0)]
        for move in moves:
            gomokuGame.make_move(move[0], move[1])
        self.assertEqual('O', gomokuGame.check_winner())

### Test Output:
# 0 errors, 4 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_check_winner_1: None != 'X'
#         test_check_winner_2: 'X' != 'O'
#         test_check_winner_3: 'O' != 'X'
#         test_check_winner_4: 'X' != 'O'


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.board, self.board_size
# method_dependencies: _check_five_in_a_row


