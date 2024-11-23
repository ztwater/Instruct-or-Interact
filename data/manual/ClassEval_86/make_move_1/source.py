class TicTacToe:
    def make_move(board, position, current_player):
        board[position] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        return board, current_player