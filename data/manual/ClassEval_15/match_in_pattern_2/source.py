class BoyerMooreSearch:
    def match_in_pattern(pattern, character):
        # Initialize the index variable to -1
        index = -1
        
        # Iterate through the pattern from right to left
        for i in range(len(pattern) - 1, -1, -1):
            # Check if the current character matches the given character
            if pattern[i] == character:
                # Update the index variable and break the loop
                index = i
                break
        
        # Return the rightmost occurrence index
        return index