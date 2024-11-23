class PushBoxGame:
    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.
    
        :return: True if the game is won, False otherwise.
        """
        def game_won():
            """
            Check if the game is won. 
            :return: True if the game is won, False otherwise.
            """
            for target in self.targets:
                if target not in self.boxes:
                    return False
            return True
    
        def move_player(row, col, direction):
            """
            Move the player to the specified direction if it's a valid move.
            :param row: int, the current row position of the player.
            :param col: int, the current column position of the player.
            :param direction: str, the direction of the player's movement. 
                It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.
            :return: tuple, the new row and column position of the player after the movement.
            """
            if direction == 'w':
                if self.map[row - 1][col] != '#':
                    row -= 1
            elif direction == 's':
                if self.map[row + 1][col] != '#':
                    row += 1
            elif direction == 'a':
                if self.map[row][col - 1] != '#':
                    col -= 1
            elif direction == 'd':
                if self.map[row][col + 1] != '#':
                    col += 1
            return row, col
    
        def move_box(row, col, direction):
            """
            Move the box to the specified direction if it's a valid move.
            :param row: int, the current row position of the box.
            :param col: int, the current column position of the box.
            :param direction: str, the direction of the box's movement. 
                It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.
            :return: tuple, the new row and column position of the box after the movement.
            """
            if direction == 'w':
                if self.map[row - 1][col] != '#' and (row - 1, col) not in self.boxes:
                    row -= 1
            elif direction == 's':
                if self.map[row + 1][col] != '#' and (row + 1, col) not in self.boxes:
                    row += 1
            elif direction == 'a':
                if self.map[row][col - 1] != '#' and (row, col - 1) not in self.boxes:
                    col -= 1
            elif direction == 'd':
                if self.map[row][col + 1] != '#' and (row, col + 1) not in self.boxes:
                    col += 1
            return row, col
    
        def update_map():
            """
            Update the map after the player and box movements.
            """
            # Clear the player and box positions on the map
            for i in range(len(self.map)):
                self.map[i] = list(self.map[i])
                for j in range(len(self.map[i])):
                    if self.map[i][j] == 'O' or self.map[i][j] == 'X':
                        self.map[i][j] = ' '
            # Update the player position on the map
            self.map[self.player_row][self.player_col] = 'O'
            # Update the box positions on the map
            for box in self.boxes:
                self.map[box[0]][box[1]] = 'X'
    
        # Move the player
        new_player_row, new_player_col = move_player(self.player_row, self.player_col, direction)
        # Move the box if there is one in front of the player
        if (new_player_row, new_player_col) in self.boxes:
            new_box_row, new_box_col = move_box(new_player_row, new_player_col, direction)
            # Update the box position if the move is valid
            if (new_box_row, new_box_col) != (new_player_row, new_player_col):
                self.boxes.remove((new_player_row, new_player_col))
                self.boxes.append((new_box_row, new_box_col))
                self.player_row, self.player_col = new_player_row, new_player_col
        else:
            self.player_row, self.player_col = new_player_row, new_player_col
    
        # Check if the game is won
        if game_won():
            print("Congratulations! You won the game!")
            return True
        else:
            return False