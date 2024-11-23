class Lemmatization:
    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'
        """
        # Create a translation table to remove punctuation
        translator = str.maketrans("", "", string.punctuation)
        
        # Remove punctuation from the sentence using the translation table
        sentence_without_punctuation = sentence.translate(translator)
        
        return sentence_without_punctuation