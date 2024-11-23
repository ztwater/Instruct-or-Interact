class MahjongConnect:
    def is_game_over(self):
        for row in self.board:
            for icon in row:
                if icon != "":
                    return False
        return True