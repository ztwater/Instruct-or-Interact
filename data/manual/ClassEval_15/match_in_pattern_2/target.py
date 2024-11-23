class BoyerMooreSearch:
    def match_in_pattern(self, char):
        # Initialize the index variable to -1
        index = -1
        
        # Iterate through the pattern from right to left
        for i in range(self.patLen - 1, -1, -1):
            # Check if the current character matches the given character
            if self.pattern[i] == char:
                # Update the index variable and break the loop
                index = i
                break
        
        # Return the rightmost occurrence index
        return index