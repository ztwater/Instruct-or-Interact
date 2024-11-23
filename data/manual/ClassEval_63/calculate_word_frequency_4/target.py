class NLPDataProcessor2:
    def calculate_word_frequency(self, words_list):
        word_frequency = Counter()
        
        # Calculate word frequency
        for words in words_list:
            word_frequency.update(words)
        
        # Sort word frequency dictionary by value in descending order
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        
        # Return top 5 word frequency dictionary
        return dict(list(sorted_word_frequency.items())[:5])