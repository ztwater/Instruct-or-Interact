class NLPDataProcessor2:
    def process_data(self, string_list):
        # Keep only English letters and spaces
        filtered_string = [''.join([char for char in string if char.isalpha() or char.isspace()]) for string in string_list]
        
        # Convert the string to lower case
        lowercased_string = [string.lower() for string in filtered_string]
        
        # Split the string into a list of words
        words_list = [string.split() for string in lowercased_string]
        
        return words_list