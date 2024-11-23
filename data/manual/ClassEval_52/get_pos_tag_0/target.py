class Lemmatization:
    def get_pos_tag(self, sentence):
        # Remove punctuations
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark part of speech tag for each word
        pos_tags = pos_tag(tokens)
        
        return [tag for _, tag in pos_tags]