class BoyerMooreSearch:
    def mismatch_in_text(self, currentPos):
        if self.patLen > self.textLen - currentPos:
            return -1
        
        for i in range(self.textLen - self.patLen - currentPos + 1):
            mismatch = False
            for j in range(self.patLen):
                if self.text[currentPos+i+j] != self.pattern[j]:
                    mismatch = True
                    break
            if not mismatch:
                return currentPos + i
        
        return -1