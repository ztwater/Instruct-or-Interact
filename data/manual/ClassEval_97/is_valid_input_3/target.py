class Words2Numbers:
    def is_valid_input(self, textnum):
        valid_words = self.units + self.tens + self.scales
        
        words = textnum.split()
        for word in words:
            if word.lower() not in valid_words:
                return False
        
        return True