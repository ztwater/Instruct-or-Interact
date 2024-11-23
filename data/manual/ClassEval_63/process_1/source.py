class NLPDataProcessor2:
    def process(string):
        # Keep only English letters and spaces
        cleaned_string = ''.join(c.lower() for c in string if c.isalpha() or c.isspace())
        
        # Split the string into a list of words
        word_list = cleaned_string.split()
        
        # Calculate word frequency
        word_frequency = {}
        for word in word_list:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
        
        # Sort word frequency dictionary by value in descending order
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        
        return sorted_word_frequency