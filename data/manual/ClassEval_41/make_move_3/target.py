class GomokuGame:
    def make_move(self, row, col):
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player (if the current player is 'X', then it becomes 'O' and vice versa).
        :param row: int, the row index of this move
        :param col: int, the column index
        return: True if the move is valid, or False otherwise.
        """
        # Check if the move is within the board boundaries
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False

        # Check if the move is valid (the cell is empty)
        if self.board[row][col] != ' ':
            return False

        # Place current player's symbol on the board
        self.board[row][col] = self.current_player

        # Change current player to the other player
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

        return True