class BoyerMooreSearch:
    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first mismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first mismatch between the pattern and the text, int, otherwise -1.
        """
        if len(self.pattern) > len(self.text):
            return -1
        
        for i in range(currentPos, len(self.text) - len(self.pattern) + 1):
            mismatch = False
            for j in range(len(self.pattern)):
                if self.text[i+j] != self.pattern[j]:
                    mismatch = True
                    break
            if not mismatch:
                return i
        
        return -1