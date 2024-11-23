class MinesweeperGame:
    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise, if the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            return True
        else:
            self.player_map[x][y] = self.minesweeper_map[x][y]
            return self.player_map