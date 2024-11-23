class TicTacToe:
    def is_board_full(board):
        for row in board:
            for cell in row:
                if cell == "":
                    return False
        return True