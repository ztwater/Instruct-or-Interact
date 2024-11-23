class MahjongConnect:
    def is_valid_move(board, pos1, pos2):
        # Check if positions are within the game board range
        if pos1[0] < 0 or pos1[0] >= len(board) or pos1[1] < 0 or pos1[1] >= len(board[0]):
            return False
        if pos2[0] < 0 or pos2[0] >= len(board) or pos2[1] < 0 or pos2[1] >= len(board[0]):
            return False
        
        # Check if the two positions are not the same
        if pos1 == pos2:
            return False
        
        # Check if the two positions have the same icon
        if board[pos1[0]][pos1[1]] != board[pos2[0]][pos2[1]]:
            return False
        
        # Check if there is a valid path between the two positions
        # (You'll need to implement this logic based on your game's rules)
        if not is_valid_path(board, pos1, pos2):
            return False
        
        return True