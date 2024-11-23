class EightPuzzle:
    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
        """
        moves = []
        
        # Find the position of the blank tile
        blank_row, blank_col = self.find_blank(state)
        
        # Check if it is possible to move up
        if blank_row > 0:
            moves.append('up')
        
        # Check if it is possible to move down
        if blank_row < 2:
            moves.append('down')
        
        # Check if it is possible to move left
        if blank_col > 0:
            moves.append('left')
        
        # Check if it is possible to move right
        if blank_col < 2:
            moves.append('right')
        
        return moves