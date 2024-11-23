class PushBoxGame:
    def init_game(self):
        """
        Initialize the game by setting the positions of the player, targets, and boxes based on the map.
        """
        self.player_pos = None
        self.targets = []
        self.boxes = []
    
        # Iterate through the map to find the positions of the player, targets, and boxes
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'O':
                    self.player_pos = (i, j)
                elif self.map[i][j] == 'G':
                    self.targets.append((i, j))
                elif self.map[i][j] == 'X':
                    self.boxes.append((i, j))