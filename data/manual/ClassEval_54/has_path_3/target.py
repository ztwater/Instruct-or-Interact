class MahjongConnect:
    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
        
        def dfs(row, col, visited):
            visited.add((row, col))
            if (row, col) == pos2:
                return True
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row >= 0 and new_row < self.BOARD_SIZE[0] and new_col >= 0 and new_col < self.BOARD_SIZE[1] and self.board[new_row][new_col] != ' ' and (new_row, new_col) not in visited:
                    if dfs(new_row, new_col, visited):
                        return True
                    
            return False
        
        visited = set()
        return dfs(pos1[0], pos1[1], visited)