class MinesweeperGame:
    def generate_playerMap(n, k):
        board = [['-' for _ in range(n)] for _ in range(n)]
        return board