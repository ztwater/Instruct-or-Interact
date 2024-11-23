class BoyerMooreSearch:
    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        if len(self.pattern) > len(self.text) - currentPos:
            return -1
        
        for i in range(len(self.pattern)):
            if self.text[currentPos + i] != self.pattern[i]:
                return currentPos + i
        
        return -1