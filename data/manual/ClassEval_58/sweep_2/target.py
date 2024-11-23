class MinesweeperGame:
    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise,if the game still continues, return the player map, list.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.sweep(1, 1)
        [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]
        """
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return self.player_map
        else:
            mine_count = self.calculate_mine_count(x, y)
            self.player_map[x][y] = mine_count
            if mine_count == 0:
                self.expand_empty_positions(x, y)
            
            if self.check_won(self.player_map):
                return True
            else:
                return self.player_map
        