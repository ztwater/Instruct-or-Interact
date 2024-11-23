class BoyerMooreSearch:
    def bad_character_heuristic(self):
        """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        """
        occurrences = []

        # Create a dictionary to store the rightmost occurrence of each character in the pattern
        bad_char_dict = {}
        for i in range(self.patLen):
            bad_char_dict[self.pattern[i]] = i

        # Start searching for the pattern in the text
        i = 0
        while i <= self.textLen - self.patLen:
            j = self.patLen - 1

            # Compare characters from right to left
            while j >= 0 and self.pattern[j] == self.text[i + j]:
                j -= 1

            # If the pattern is found, add the occurrence index to the list
            if j < 0:
                occurrences.append(i)
                i += self.patLen
            else:
                # Shift the pattern to align the bad character with its rightmost occurrence in the pattern
                shift = max(1, j - bad_char_dict.get(self.text[i + j], -1))
                i += shift

        return occurrences