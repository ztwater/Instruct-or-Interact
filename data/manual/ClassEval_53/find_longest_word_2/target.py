class LongestWord:
    def find_longest_word(self, sentence):
        # Remove punctuation marks
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Split sentence into a list of words
        words = sentence.split()
        
        # Find the longest word that is in the self.word_list
        longest_word = ''
        for word in words:
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
        
        return longest_word