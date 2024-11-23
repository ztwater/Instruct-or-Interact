class MahjongConnect:
    def create_board(self):
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.create_board()
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
        board = []
        for _ in range(self.BOARD_SIZE[0]):
            row = []
            for _ in range(self.BOARD_SIZE[1]):
                row.append(self.ICONS)
            board.append(row)
        return board
