class MahjongConnect:
    def is_valid_move(self, pos1, pos2):
        # Check if positions are within the game board range
        if pos1[0] < 0 or pos1[0] >= len(self.board) or pos1[1] < 0 or pos1[1] >= len(self.board[0]):
            return False
        if pos2[0] < 0 or pos2[0] >= len(self.board) or pos2[1] < 0 or pos2[1] >= len(self.board[0]):
            return False
    
        # Check if the two positions are not the same
        if pos1 == pos2:
            return False
    
        # Check if the two positions have the same icon
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
    
        # Check if there is a valid path between the two positions
        if not self.has_path(pos1, pos2):
            return False
    
        return True