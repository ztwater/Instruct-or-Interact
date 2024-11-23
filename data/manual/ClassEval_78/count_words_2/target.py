class SplitSentence:
    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
        # Split the sentence into words using spaces as separators
        words = sentence.split(" ")
        
        # Initialize a counter for the number of words
        count = 0
        
        # Iterate through each word in the sentence
        for word in words:
            # Check if the word is not empty (i.e., not just spaces)
            if word.strip() != "":
                # Increment the counter
                count += 1
        
        # Return the number of words
        return count