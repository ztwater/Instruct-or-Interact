class MinesweeperGame:
    def sweep(self, x, y):
        """
        Sweeps the given position.
        :param x: The x coordinate of the position, int.
        :param y: The y coordinate of the position, int.
        :return: True if the player has won the game, False otherwise, if the game still continues, return the player map, list.
        """
        if self.minesweeper_map[x][y] == 'X':
            self.player_map[x][y] = 'X'
            return False

        self.player_map[x][y] = self.minesweeper_map[x][y]

        if self.minesweeper_map[x][y] == 0:
            visited = set()
            self.explore(x, y, visited)

        return self.check_won()
