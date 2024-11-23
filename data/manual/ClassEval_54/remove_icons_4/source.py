class MahjongConnect:
    def remove_icons(board):
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
    
        def dfs(row, col, icon):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if visited[row][col] or board[row][col] != icon:
                return
    
            visited[row][col] = True
            board[row][col] = None
    
            dfs(row - 1, col, icon)  # check above
            dfs(row + 1, col, icon)  # check below
            dfs(row, col - 1, icon)  # check left
            dfs(row, col + 1, icon)  # check right
    
        for row in range(rows):
            for col in range(cols):
                if board[row][col] is not None:
                    dfs(row, col, board[row][col])
    
        # Shift down the remaining icons
        for col in range(cols):
            empty_rows = [row for row in range(rows) if board[row][col] is None]
            non_empty_rows = [row for row in range(rows) if board[row][col] is not None]
            for empty_row, non_empty_row in zip(empty_rows, non_empty_rows):
                board[empty_row][col], board[non_empty_row][col] = board[non_empty_row][col], board[empty_row][col]
    
        return board