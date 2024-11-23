class PushBoxGame:
    def move(self, direction):
        # Move the player based on the specified direction
        if direction == "w":
            new_row = self.player_row - 1
            new_col = self.player_col
        elif direction == "s":
            new_row = self.player_row + 1
            new_col = self.player_col
        elif direction == "a":
            new_row = self.player_row
            new_col = self.player_col - 1
        elif direction == "d":
            new_row = self.player_row
            new_col = self.player_col + 1
    
        # Check if the new position is valid
        if self.map[new_row][new_col] == "#":
            return False
    
        # Check if there is a box at the new position
        if self.map[new_row][new_col] == "X":
            # Calculate the new position of the box
            new_box_row = new_row + (new_row - self.player_row)
            new_box_col = new_col + (new_col - self.player_col)
    
            # Check if the new position of the box is valid
            if self.map[new_box_row][new_box_col] == "#" or self.map[new_box_row][new_box_col] == "X":
                return False
    
            # Move the box to the new position
            self.boxes.remove((new_row, new_col))
            self.boxes.append((new_box_row, new_box_col))
            self.map[new_row] = self.map[new_row][:new_col] + " " + self.map[new_row][new_col+1:]
            self.map[new_box_row] = self.map[new_box_row][:new_box_col] + "X" + self.map[new_box_row][new_box_col+1:]
    
        # Move the player to the new position
        self.map[self.player_row] = self.map[self.player_row][:self.player_col] + " " + self.map[self.player_row][self.player_col+1:]
        self.map[new_row] = self.map[new_row][:new_col] + "O" + self.map[new_row][new_col+1:]
        self.player_row = new_row
        self.player_col = new_col
    
        # Check if the game is won
        if self.check_win():
            print("Congratulations! You won the game!")
            return True
    
        return False