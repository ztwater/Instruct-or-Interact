class Lemmatization:
    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        """
        # Remove punctuations from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_tokens = self.get_pos_tag(tokens)
        
        # Lemmatize the words
        lemmatized_tokens = [self.lemmatizer.lemmatize(token, tag) for token, tag in tagged_tokens]
        
        return lemmatized_tokens