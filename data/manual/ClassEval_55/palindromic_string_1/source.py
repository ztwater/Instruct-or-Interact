class Manacher:
    def palindromic_string(s):
        if len(s) < 2:
            return s
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            len1 = expand_around_center(s, i, i)
            len2 = expand_around_center(s, i, i+1)
            length = max(len1, len2)
            
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        return s[start:end+1]
    