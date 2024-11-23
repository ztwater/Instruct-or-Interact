class BoyerMooreSearch:
    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        """
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