class PushBoxGame:
    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.
    
        :return: True if the game is won, False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
        def move_player(row_offset, col_offset):
            new_row = self.player_row + row_offset
            new_col = self.player_col + col_offset
            next_cell = self.map[new_row][new_col]
            
            if next_cell not in ['#', 'X']:
                if next_cell == ' ':
                    self.map[new_row] = self.map[new_row][:new_col] + 'O' + self.map[new_row][new_col + 1:]
                    self.player_row = new_row
                    self.player_col = new_col
                elif next_cell == 'G':
                    self.map[new_row] = self.map[new_row][:new_col] + 'O' + self.map[new_row][new_col + 1:]
                    self.player_row = new_row
                    self.player_col = new_col
                    self.target_count -= 1
                
                return True
            
            return False
        
        if direction == 'w':
            return move_player(-1, 0)
        elif direction == 's':
            return move_player(1, 0)
        elif direction == 'a':
            return move_player(0, -1)
        elif direction == 'd':
            return move_player(0, 1)