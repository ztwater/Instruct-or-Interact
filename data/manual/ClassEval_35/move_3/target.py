class EightPuzzle:
    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        # Find the coordinates of the blank tile
        blank_row, blank_col = self.find_blank(state)

        # Create a copy of the state
        new_state = [row.copy() for row in state]

        # Make the board move forward in the given direction
        if direction == 'up':
            new_state[blank_row][blank_col], new_state[blank_row-1][blank_col] = new_state[blank_row-1][blank_col], new_state[blank_row][blank_col]
        elif direction == 'down':
            new_state[blank_row][blank_col], new_state[blank_row+1][blank_col] = new_state[blank_row+1][blank_col], new_state[blank_row][blank_col]
        elif direction == 'left':
            new_state[blank_row][blank_col], new_state[blank_row][blank_col-1] = new_state[blank_row][blank_col-1], new_state[blank_row][blank_col]
        elif direction == 'right':
            new_state[blank_row][blank_col], new_state[blank_row][blank_col+1] = new_state[blank_row][blank_col+1], new_state[blank_row][blank_col]

        return new_state