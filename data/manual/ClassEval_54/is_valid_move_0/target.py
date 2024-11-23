class MahjongConnect:
    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        # Check if positions are within the game board range
        if pos1[0] < 0 or pos1[0] >= self.BOARD_SIZE[0] or pos1[1] < 0 or pos1[1] >= self.BOARD_SIZE[1]:
            return False
        if pos2[0] < 0 or pos2[0] >= self.BOARD_SIZE[0] or pos2[1] < 0 or pos2[1] >= self.BOARD_SIZE[1]:
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