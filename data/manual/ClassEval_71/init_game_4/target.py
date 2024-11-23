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
                    self.player_row = i
                    self.player_col = j
                elif self.map[i][j] == 'G':
                    target_pos.append((i, j))
                    self.targets.append((i, j))
                    self.target_count += 1
                elif self.map[i][j] == 'X':
                    box_pos.append((i, j))
                    self.boxes.append((i, j))
    
        # Return the positions as a tuple
        return player_pos, target_pos, box_pos
    