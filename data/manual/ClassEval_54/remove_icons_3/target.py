class MahjongConnect:
    def remove_icons(self, pos1, pos2):
        rows = self.BOARD_SIZE[0]
        cols = self.BOARD_SIZE[1]
        visited = [[False] * cols for _ in range(rows)]
    
        def dfs(row, col, icon):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if visited[row][col] or self.board[row][col] != icon:
                return
    
            visited[row][col] = True
            self.board[row][col] = None
    
            dfs(row - 1, col, icon)  # check above
            dfs(row + 1, col, icon)  # check below
            dfs(row, col - 1, icon)  # check left
            dfs(row, col + 1, icon)  # check right
    
        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] is not None:
                    dfs(row, col, self.board[row][col])
    
        # Shift down the remaining icons
        for col in range(cols):
            empty_rows = [row for row in range(rows) if self.board[row][col] is None]
            non_empty_rows = [row for row in range(rows) if self.board[row][col] is not None]
            for empty_row, non_empty_row in zip(empty_rows, non_empty_rows):
                self.board[empty_row][col], self.board[non_empty_row][col] = self.board[non_empty_row][col], self.board[empty_row][col]
    
        return None