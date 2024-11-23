class Manacher:
    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        s = self.input_string
        
        if len(s) < 2:
            return s
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            len1 = self.palindromic_length(i, i, s)
            len2 = self.palindromic_length(i, i+1, s)
            length = max(len1, len2)
            
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        return s[start:end+1]
