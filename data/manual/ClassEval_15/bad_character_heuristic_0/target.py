class BoyerMooreSearch:
    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        pattern_length = self.patLen
        text_length = self.textLen
        occurrences = []
    
        # Create a dictionary to store the rightmost occurrence of each character in the pattern
        bad_char_dict = {}
        for i in range(pattern_length):
            bad_char_dict[self.pattern[i]] = i
    
        # Start searching for the pattern in the text
        i = 0
        while i <= text_length - pattern_length:
            j = pattern_length - 1
    
            # Compare characters from right to left
            while j >= 0 and self.pattern[j] == self.text[i + j]:
                j -= 1
    
            # If the pattern is found, add the occurrence index to the list
            if j < 0:
                occurrences.append(i)
                i += pattern_length
            else:
                # Shift the pattern to align the bad character with its rightmost occurrence in the pattern
                shift = max(1, j - bad_char_dict.get(self.text[i + j], -1))
                i += shift
    
        return occurrences