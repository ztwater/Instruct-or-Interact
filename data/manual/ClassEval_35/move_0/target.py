class EightPuzzle:
    def move(self, state, direction):
        """
        Find the blank block, then makes the board move forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        """
        # Find the blank block
        blank = self.find_blank(state)
    
        # Create a new state to store the updated board after moving
        new_state = [row[:] for row in state]
    
        # Make the board move forward in the given direction
        if direction == 'up':
            if blank[0] > 0:
                new_state[blank[0]][blank[1]], new_state[blank[0]-1][blank[1]] = new_state[blank[0]-1][blank[1]], new_state[blank[0]][blank[1]]
        elif direction == 'down':
            if blank[0] < len(state) - 1:
                new_state[blank[0]][blank[1]], new_state[blank[0]+1][blank[1]] = new_state[blank[0]+1][blank[1]], new_state[blank[0]][blank[1]]
        elif direction == 'left':
            if blank[1] > 0:
                new_state[blank[0]][blank[1]], new_state[blank[0]][blank[1]-1] = new_state[blank[0]][blank[1]-1], new_state[blank[0]][blank[1]]
        elif direction == 'right':
            if blank[1] < len(state[0]) - 1:
                new_state[blank[0]][blank[1]], new_state[blank[0]][blank[1]+1] = new_state[blank[0]][blank[1]+1], new_state[blank[0]][blank[1]]
    
        return new_state