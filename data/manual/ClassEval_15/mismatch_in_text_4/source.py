class BoyerMooreSearch:
    def mismatch_in_text(pattern, text):
        if len(pattern) > len(text):
            return -1
        
        for i in range(len(text) - len(pattern) + 1):
            mismatch = False
            for j in range(len(pattern)):
                if text[i+j] != pattern[j]:
                    mismatch = True
                    break
            if not mismatch:
                return i
        
        return -1