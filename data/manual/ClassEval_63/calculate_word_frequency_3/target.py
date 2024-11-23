class NLPDataProcessor2:
    def calculate_word_frequency(self, words_list):
        word_frequency = {}
        
        # Calculate word frequency
        for words in words_list:
            for word in words:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
        
        # Sort word frequency dictionary by value in descending order
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        
        return dict(list(sorted_word_frequency.items())[:5])