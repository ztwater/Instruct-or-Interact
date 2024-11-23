class MahjongConnect:
    def create_board(size, icons):
        board = []
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(icons)
            board.append(row)
        return board