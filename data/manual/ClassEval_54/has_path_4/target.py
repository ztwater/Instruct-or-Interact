class MahjongConnect:
    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        """
        
        # Check if the positions are valid
        if not self.is_valid_position(pos1) or not self.is_valid_position(pos2):
            return False
        
        # Check if the icons at the positions are the same
        if self.board[pos1[0]][pos1[1]] != self.board[pos2[0]][pos2[1]]:
            return False
        
        # Check if the positions are adjacent
        if not self.is_adjacent(pos1, pos2):
            return False
        
        # Check if there is a clear path between the positions
        if not self.is_clear_path(pos1, pos2):
            return False
        
        return True
