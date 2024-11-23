class EightPuzzle:
    def move(board, direction):
        # Find the blank block
        blank = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    blank = (i, j)
                    break
            if blank:
                break
        
        # Make the board move forward in the given direction
        if direction == 'up':
            if blank[0] > 0:
                board[blank[0]][blank[1]], board[blank[0]-1][blank[1]] = board[blank[0]-1][blank[1]], board[blank[0]][blank[1]]
        elif direction == 'down':
            if blank[0] < len(board) - 1:
                board[blank[0]][blank[1]], board[blank[0]+1][blank[1]] = board[blank[0]+1][blank[1]], board[blank[0]][blank[1]]
        elif direction == 'left':
            if blank[1] > 0:
                board[blank[0]][blank[1]], board[blank[0]][blank[1]-1] = board[blank[0]][blank[1]-1], board[blank[0]][blank[1]]
        elif direction == 'right':
            if blank[1] < len(board[0]) - 1:
                board[blank[0]][blank[1]], board[blank[0]][blank[1]+1] = board[blank[0]][blank[1]+1], board[blank[0]][blank[1]]
        
        return board