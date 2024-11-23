class BoyerMooreSearch:
    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2

        """
        text = self.text
        pattern = self.pattern
        
        if len(pattern) > len(text):
            return -1
        
        for i in range(currentPos, len(text) - len(pattern) + 1):
            mismatch = False
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    mismatch = True
                    break
            if not mismatch:
                return i
        
        return -1