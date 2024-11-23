class Lemmatization:
    def lemmatize_sentence(self, sentence):
        # Remove punctuations from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_tokens = self.get_pos_tag(tokens)
        
        # Lemmatize the words
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token, tag in tagged_tokens]
        
        return lemmatized_tokens