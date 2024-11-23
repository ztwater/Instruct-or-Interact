class TicTacToe:
    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        """
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True