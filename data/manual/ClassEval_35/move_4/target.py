class EightPuzzle:
    def move(self, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move('left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        # Find the blank block
        blank = None
        for i in range(len(self.initial_state)):
            for j in range(len(self.initial_state[i])):
                if self.initial_state[i][j] == 0:
                    blank = (i, j)
                    break
            if blank:
                break

        # Make the board move forward in the given direction
        if direction == 'up':
            if blank[0] > 0:
                self.initial_state[blank[0]][blank[1]], self.initial_state[blank[0] - 1][blank[1]] = self.initial_state[blank[0] - 1][blank[1]], self.initial_state[blank[0]][blank[1]]
        elif direction == 'down':
            if blank[0] < len(self.initial_state) - 1:
                self.initial_state[blank[0]][blank[1]], self.initial_state[blank[0] + 1][blank[1]] = self.initial_state[blank[0] + 1][blank[1]], self.initial_state[blank[0]][blank[1]]
        elif direction == 'left':
            if blank[1] > 0:
                self.initial_state[blank[0]][blank[1]], self.initial_state[blank[0]][blank[1] - 1] = self.initial_state[blank[0]][blank[1] - 1], self.initial_state[blank[0]][blank[1]]
        elif direction == 'right':
            if blank[1] < len(self.initial_state[0]) - 1:
                self.initial_state[blank[0]][blank[1]], self.initial_state[blank[0]][blank[1] + 1] = self.initial_state[blank[0]][blank[1] + 1], self.initial_state[blank[0]][blank[1]]

        return self.initial_state