class EightPuzzle:
    def solve(initial_state, goal_state):
        # Create a queue to store the states to be explored
        queue = deque()
        # Create a set to store the visited states
        visited = set()
    
        # Add the initial state to the queue
        queue.append((initial_state, []))
    
        while queue:
            state, path = queue.popleft()
    
            # Check if the current state is the goal state
            if state == goal_state:
                return path
    
            # Add the current state to the visited set
            visited.add(state)
    
            # Generate all possible next states from the current state
            next_states = generate_next_states(state)
    
            for next_state in next_states:
                # Check if the next state has not been visited
                if next_state not in visited:
                    # Add the next state and the path to reach it to the queue
                    queue.append((next_state, path + [next_state]))
    
        # If no path is found, return None
        return None
    