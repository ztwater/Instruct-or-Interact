class NLPDataProcessor2:
    def process_data(string):
        # Keep only English letters and spaces
        filtered_string = ''.join([char for char in string if char.isalpha() or char.isspace()])

        # Convert the string to lower case
        lowercased_string = filtered_string.lower()

        # Split the string into a list of words
        word_list = lowercased_string.split()

        return word_list
