class Lemmatization:
    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        translator = str.maketrans("", "", string.punctuation)
        text_without_punctuation = sentence.translate(translator)
        return text_without_punctuation
