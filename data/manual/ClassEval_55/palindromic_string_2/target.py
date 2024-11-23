class Manacher:
    def palindromic_string(self):
        if len(self.input_string) < 2:
            return self.input_string
        
        start = 0
        end = 0
        
        for i in range(len(self.input_string)):
            len1 = self.palindromic_length(i, i, self.input_string)
            len2 = self.palindromic_length(i, i+1, self.input_string)
            length = max(len1, len2)
            
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        
        return self.input_string[start:end+1]
    