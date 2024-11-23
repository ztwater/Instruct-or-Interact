class MahjongConnect:
    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        """
        def dfs(x, y, visited):
            # Check if position (x, y) is within the board boundaries
            if x < 0 or x >= self.BOARD_SIZE[0] or y < 0 or y >= self.BOARD_SIZE[1]:
                return False
            
            # Check if position (x, y) is already visited
            if (x, y) in visited:
                return False
            
            # Check if the icons at positions (x, y) and pos2 are the same
            if self.board[x][y] == self.board[pos2[0]][pos2[1]]:
                # If the positions are adjacent, return True
                if abs(x - pos2[0]) + abs(y - pos2[1]) == 1:
                    return True
                
                # Mark position (x, y) as visited
                visited.add((x, y))
                
                # Recursively check if there is a path from (x, y) to pos2
                return dfs(x + 1, y, visited) or dfs(x - 1, y, visited) or dfs(x, y + 1, visited) or dfs(x, y - 1, visited)
            
            return False
    
        # Perform depth-first search from pos1 to check if there is a path to pos2
        return dfs(pos1[0], pos1[1], set())