class MinesweeperGame:
    def generate_mine_sweeper_map(n, k):
        import random
        
        # Create an empty board
        board = [['0' for _ in range(n)] for _ in range(n)]
        
        # Place the mines randomly
        mines_placed = 0
        while mines_placed < k:
            row = random.randint(0, n-1)
            col = random.randint(0, n-1)
            
            # Check if the current position is already a mine
            if board[row][col] != 'X':
                board[row][col] = 'X'
                mines_placed += 1
        
        # Update the numbers around the mines
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                
                # Count the number of mines around the current position
                count = 0
                for x in range(max(0, i-1), min(n, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        if board[x][y] == 'X':
                            count += 1
                
                # Update the current position with the count
                board[i][j] = str(count)
        
        # Return the generated minesweeper map
        return board