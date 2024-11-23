class MinesweeperGame:
    def check_won(player_map):
        for row in player_map:
            for cell in row:
                if cell != 'M':
                    return False
        return True