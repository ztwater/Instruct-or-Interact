class EightPuzzle:
    def find_blank(current_state):
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] == 0:
                    return (i, j)