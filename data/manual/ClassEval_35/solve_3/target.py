class EightPuzzle:
    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
        Traversal the possible_moves list and invoke move method to get several new states. Then append them.
        Redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['right']
        """
        # Create a queue to store the states to be explored
        queue = deque()
        # Create a set to store the visited states
        visited = set()
    
        # Add the initial state to the queue
        queue.append((self.initial_state, []))
    
        while queue:
            state, path = queue.popleft()
    
            # Check if the current state is the goal state
            if state == self.goal_state:
                return path
    
            # Add the current state to the visited set
            visited.add(state)
    
            # Generate all possible next states from the current state
            next_states = self.get_possible_moves(state)
    
            for next_state in next_states:
                # Check if the next state has not been visited
                if next_state not in visited:
                    # Add the next state and the path to reach it to the queue
                    queue.append((next_state, path + [next_state]))
    
        # If no path is found, return None
        return None