class NLPDataProcessor2:
    def process(self, string_list):
        # Keep only English letters and spaces
        cleaned_string = ''.join(c.lower() for string in string_list for c in string if c.isalpha() or c.isspace())
        
        # Split the string into a list of words
        word_list = cleaned_string.split()
        
        # Calculate word frequency
        word_frequency = self.calculate_word_frequency(word_list)
        
        # Sort word frequency dictionary by value in descending order
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        
        # Return top 5 word frequency dictionary
        return dict(Counter(sorted_word_frequency).most_common(5))
    