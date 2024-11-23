class NumberWordFormatter:
    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        digit_to_word = {
            "0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine"
        }
        
        number_str = str(s)
        
        if len(number_str) != 2:
            return "Invalid input. Please enter a two-digit number."
        
        tens_digit = number_str[0]
        ones_digit = number_str[1]
        
        tens_word = digit_to_word[tens_digit]
        ones_word = digit_to_word[ones_digit]
        
        return tens_word + " " + ones_word