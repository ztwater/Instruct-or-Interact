class NumberWordFormatter:
    def format_string(number):
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
        for digit in number:
            if digit in words:
                result.append(words[digit])
        
        # Join the words together and return the result
        return ' '.join(result)