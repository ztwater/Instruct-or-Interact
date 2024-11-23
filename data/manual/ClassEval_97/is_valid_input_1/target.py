class Words2Numbers:
    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """

        valid_words = self.units + self.tens + self.scales
        
        words = textnum.split()
        for word in words:
            if word.lower() not in valid_words:
                return False
        
        return True