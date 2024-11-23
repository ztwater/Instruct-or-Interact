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
        # Define a dictionary to map each digit to its corresponding word
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
        
        # Convert the number to a string
        number_str = str(s)
        
        # Check if the number is a two-digit number
        if len(number_str) != 2:
            return "Invalid input. Please enter a two-digit number."
        
        # Get the tens digit and ones digit
        tens_digit = number_str[0]
        ones_digit = number_str[1]
        
        # Convert the tens digit and ones digit to words using the dictionary
        tens_word = digit_to_word[tens_digit]
        ones_word = digit_to_word[ones_digit]
        
        # Return the words format of the two-digit number
        return tens_word + " " + ones_word
