class PushBoxGame:
    def init_game(self):
        player_pos = None
        target_pos = []
        box_pos = []
    
        # Iterate through the map to find the positions of the player, targets, and boxes
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'O':
                    player_pos = (i, j)
                elif self.map[i][j] == 'G':
                    target_pos.append((i, j))
                elif self.map[i][j] == 'X':
                    box_pos.append((i, j))
    
        self.player_row = player_pos[0]
        self.player_col = player_pos[1]
        self.targets = target_pos
        self.boxes = box_pos