class PushBoxGame:
    def init_game(map):
        player_pos = None
        target_pos = []
        box_pos = []
    
        # Iterate through the map to find the positions of the player, targets, and boxes
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 'P':
                    player_pos = (i, j)
                elif map[i][j] == 'T':
                    target_pos.append((i, j))
                elif map[i][j] == 'B':
                    box_pos.append((i, j))
    
        # Return the positions as a tuple
        return player_pos, target_pos, box_pos