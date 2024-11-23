class SplitSentence:
    def count_words(sentence):
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