class NumberWordFormatter:
    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        """
        # Define a dictionary to map numbers to words
        words = {
            '0': 'zero',
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine'
        }
        
        # Convert each digit in the string to its corresponding word
        result = []
        for digit in x:
            if digit in words:
                result.append(words[digit])
        
        # Join the words together and return the result
        return ' '.join(result).upper() + " ONLY"