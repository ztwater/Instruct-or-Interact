class Lemmatization:
    def remove_punctuation(text):
        # Create a translation table to remove punctuation
        translator = str.maketrans("", "", string.punctuation)
        
        # Remove punctuation from the text using the translation table
        text_without_punctuation = text.translate(translator)
        
        return text_without_punctuation