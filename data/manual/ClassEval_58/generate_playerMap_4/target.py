class MinesweeperGame:
    def generate_playerMap(self):
        """
        Generates a player map with the given size of the board, the given parameter n is the size of the board,the size of the board is n*n,the parameter k is the number of mines,'-' represents the unknown position.
        :return: The player map, list.
        """
        board = [['-' for _ in range(self.n)] for _ in range(self.n)]
        return board