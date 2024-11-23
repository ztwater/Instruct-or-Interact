class MinesweeperGame:
    def check_won(self, player_map):
        """
        Checks whether the player has won the game, if there are just mines in the player map, return True, otherwise return False.
        :return: True if the player has won the game, False otherwise.
        """
        for row in player_map:
            for cell in row:
                if cell != 'M':
                    return False
        return True