class Manacher:
    def palindromic_length(self, center, diff, string):
        # Base case: if the center is out of bounds or the characters at the center and diff positions are not equal, return 0
        if center < 0 or center >= len(string) or string[center] != string[center + diff]:
            return 0
        
        # Recursive case: increment the length by 2 (since the palindromic substring includes the center and diff positions)
        # and recursively call the function with the updated center and diff values
        return 2 + self.palindromic_length(center - 1, diff + 1, string)

