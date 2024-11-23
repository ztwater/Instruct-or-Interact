class MinesweeperGame:
    def check_won(self, player_map):
        """
        Checks whether the player has won the game, if there are just mines in the player map, return True, otherwise return False.
        :return: True if the player has won the game, False otherwise.
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        >>> minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        >>> minesweeper_game.check_won(minesweeper_game.player_map)
        False

        """
        for row in player_map:
            for cell in row:
                if cell != 'M':
                    return False
        return True