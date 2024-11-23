class MahjongConnect:
    def is_game_over(game_board):
        for row in game_board:
            for icon in row:
                if icon != "":
                    return False
        return True