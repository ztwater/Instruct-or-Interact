class EightPuzzle:
    def get_possible_moves(self, state):
        possible_moves = []
        row, col = self.find_blank(state)
    
        if row > 0:
            possible_moves.append('up')
        if row < 2:
            possible_moves.append('down')
        if col > 0:
            possible_moves.append('left')
        if col < 2:
            possible_moves.append('right')
    
        return possible_moves