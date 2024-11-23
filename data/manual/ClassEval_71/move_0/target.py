class PushBoxGame:
    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.
    
        :return: True if the game is won, False otherwise.
        """
        def move_player(row, col, row_offset, col_offset):
            new_row = row + row_offset
            new_col = col + col_offset
    
            # Check if the new position is valid
            if self.map[new_row][new_col] == "#":
                return False
    
            # Move the player to the new position
            self.map[row][col] = " "
            self.map[new_row][new_col] = "O"
    
            # Update the player's position
            self.player_row = new_row
            self.player_col = new_col
    
            return True
    
        # Move the player based on the specified direction
        if direction == "w":
            return move_player(self.player_row, self.player_col, -1, 0)
        elif direction == "s":
            return move_player(self.player_row, self.player_col, 1, 0)
        elif direction == "a":
            return move_player(self.player_row, self.player_col, 0, -1)
        elif direction == "d":
            return move_player(self.player_row, self.player_col, 0, 1)