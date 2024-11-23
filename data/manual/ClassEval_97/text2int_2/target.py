class Words2Numbers:
    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
        # Create a dictionary to map word strings to integers
        word_to_int = {
            'zero': '0',
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }
        
        # Split the word string into individual words
        words = textnum.split()
        
        # Convert each word to its corresponding integer and join them together
        int_string = ''.join(word_to_int[word] for word in words)
        
        return int_string