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
        
        # Get the icons at the specified positions
        icon1 = self.board[pos1[0]][pos1[1]]
        icon2 = self.board[pos2[0]][pos2[1]]
        
        # Check if icon1 and icon2 are the same
        if icon1 == icon2:
            return True
        
        # Check if icon1 and icon2 are connected
        # Return True if there is a path between them, False otherwise
    
        def dfs(x, y, visited):
            # Check if the position is out of bounds or already visited
            if x < 0 or x >= self.BOARD_SIZE[0] or y < 0 or y >= self.BOARD_SIZE[1] or visited[x][y]:
                return False
            
            # Mark the position as visited
            visited[x][y] = True
            
            # Check if the current icon is equal to icon2
            if self.board[x][y] == icon2:
                return True
            
            # Check if there is a path from the current position to icon2
            if (self.board[x][y] == icon1) and (dfs(x+1, y, visited) or dfs(x-1, y, visited) or dfs(x, y+1, visited) or dfs(x, y-1, visited)):
                return True
            
            return False
    
        # Create a visited array to keep track of visited positions
        visited = [[False] * self.BOARD_SIZE[1] for _ in range(self.BOARD_SIZE[0])]
        
        # Call the depth-first search function starting from pos1
        return dfs(pos1[0], pos1[1], visited)