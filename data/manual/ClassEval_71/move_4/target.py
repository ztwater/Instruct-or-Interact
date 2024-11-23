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
            Check if the game is won by comparing the positions of the boxes with the target positions.
            :return: bool, True if the game is won, False otherwise.
            """
            for box in self.boxes:
                if box not in self.targets:
                    return False
            return True
        
        def move_left():
            """
            Move the player to the left.
            """
            if self.map[self.player_row][self.player_col-1] != '#':
                if self.map[self.player_row][self.player_col-1] == ' ':
                    self.map[self.player_row][self.player_col] = ' '
                    self.map[self.player_row][self.player_col-1] = 'O'
                    self.player_col -= 1
                elif self.map[self.player_row][self.player_col-1] == 'X':
                    if self.map[self.player_row][self.player_col-2] == ' ':
                        self.map[self.player_row][self.player_col] = ' '
                        self.map[self.player_row][self.player_col-1] = 'O'
                        self.map[self.player_row][self.player_col-2] = 'X'
                        self.player_col -= 1
        
        def move_right():
            """
            Move the player to the right.
            """
            if self.map[self.player_row][self.player_col+1] != '#':
                if self.map[self.player_row][self.player_col+1] == ' ':
                    self.map[self.player_row][self.player_col] = ' '
                    self.map[self.player_row][self.player_col+1] = 'O'
                    self.player_col += 1
                elif self.map[self.player_row][self.player_col+1] == 'X':
                    if self.map[self.player_row][self.player_col+2] == ' ':
                        self.map[self.player_row][self.player_col] = ' '
                        self.map[self.player_row][self.player_col+1] = 'O'
                        self.map[self.player_row][self.player_col+2] = 'X'
                        self.player_col += 1
        
        def move_up():
            """
            Move the player up.
            """
            if self.map[self.player_row-1][self.player_col] != '#':
                if self.map[self.player_row-1][self.player_col] == ' ':
                    self.map[self.player_row][self.player_col] = ' '
                    self.map[self.player_row-1][self.player_col] = 'O'
                    self.player_row -= 1
                elif self.map[self.player_row-1][self.player_col] == 'X':
                    if self.map[self.player_row-2][self.player_col] == ' ':
                        self.map[self.player_row][self.player_col] = ' '
                        self.map[self.player_row-1][self.player_col] = 'O'
                        self.map[self.player_row-2][self.player_col] = 'X'
                        self.player_row -= 1
        
        def move_down():
            """
            Move the player down.
            """
            if self.map[self.player_row+1][self.player_col] != '#':
                if self.map[self.player_row+1][self.player_col] == ' ':
                    self.map[self.player_row][self.player_col] = ' '
                    self.map[self.player_row+1][self.player_col] = 'O'
                    self.player_row += 1
                elif self.map[self.player_row+1][self.player_col] == 'X':
                    if self.map[self.player_row+2][self.player_col] == ' ':
                        self.map[self.player_row][self.player_col] = ' '
                        self.map[self.player_row+1][self.player_col] = 'O'
                        self.map[self.player_row+2][self.player_col] = 'X'
                        self.player_row += 1
        
        if direction == 'w':
            move_up()
        elif direction == 's':
            move_down()
        elif direction == 'a':
            move_left()
        elif direction == 'd':
            move_right()

        # Check if the game is won
        if game_won():
            print("Congratulations! You won the game!")
            return True
        else:
            return False