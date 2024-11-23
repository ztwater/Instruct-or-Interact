class NLPDataProcessor2:
    def process_data(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        >>> NLPDataProcessor.process_data(['This is a test.'])
        [['this', 'is', 'a', 'test']]
        """
        words_list = []
        for string in string_list:
            # Keep only English letters and spaces
            filtered_string = ''.join([char for char in string if char.isalpha() or char.isspace()])
            
            # Convert the string to lower case
            lowercased_string = filtered_string.lower()
            
            # Split the string into a list of words
            word_list = lowercased_string.split()
            
            words_list.append(word_list)
        
        return words_list