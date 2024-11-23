class NumberWordFormatter:
    def format(number):
        # Define a dictionary to map numbers to their word format
        words = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            # Add more mappings as needed
        }
        
        # Convert the number to its word format
        if number in words:
            return words[number]
        else:
            return 'Number not supported'