class EightPuzzle:
    def get_possible_moves(self, state):
        possible_moves = []
        blank_row, blank_col = self.find_blank(state)

        if blank_row > 0:
            possible_moves.append('up')
        if blank_row < 2:
            possible_moves.append('down')
        if blank_col > 0:
            possible_moves.append('left')
        if blank_col < 2:
            possible_moves.append('right')

        return possible_moves