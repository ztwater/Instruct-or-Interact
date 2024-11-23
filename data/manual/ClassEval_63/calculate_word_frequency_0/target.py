class NLPDataProcessor2:
    def calculate_word_frequency(self, words_list):
        word_frequency = {}

        # Join all words in words_list into a single list of words
        words = [word for sublist in words_list for word in sublist]
        
        # Calculate word frequency
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
        
        # Sort word frequency dictionary by value in descending order
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        
        # Return top 5 word frequency dictionary
        return dict(list(sorted_word_frequency.items())[:5])