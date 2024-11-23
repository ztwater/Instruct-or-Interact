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
        rows = len(state)
        cols = len(state[0])
        blank_row, blank_col = self.find_blank(state)

        # Check if moving up is possible
        if blank_row - 1 >= 0:
            moves.append('up')

        # Check if moving down is possible
        if blank_row + 1 < rows:
            moves.append('down')

        # Check if moving left is possible
        if blank_col - 1 >= 0:
            moves.append('left')

        # Check if moving right is possible
        if blank_col + 1 < cols:
            moves.append('right')

        return moves