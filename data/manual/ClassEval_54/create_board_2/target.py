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
        size = self.BOARD_SIZE[0]
        icons = self.ICONS
        board = []
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(icons)
            board.append(row)
        return board