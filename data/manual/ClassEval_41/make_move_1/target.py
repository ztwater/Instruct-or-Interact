class GomokuGame:
    def make_move(self, row, col):
        """
        Makes a move at the given row and column.
        If the move is valid, it places the current player's symbol on the board
        and changes the current player to the other player (if the current player is 'X', then it becomes 'O' and vice versa).
        :param row: int, the row index of this move
        :param col: int, the column index
        return: True if the move is valid, or False otherwise.
        >>> gomokuGame = GomokuGame(10)
        >>> gomokuGame.make_move(5, 5)
        True
        >>> gomokuGame.make_move(5, 5)
        False
        """
        if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
            return False
        
        if self.board[row][col] != ' ':
            return False
        
        self.board[row][col] = self.current_player
        
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        
        return True