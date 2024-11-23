class Lemmatization:
    def get_pos_tag(self, sentence):
        # Remove punctuations
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark part of speech tag for each word
        pos_tags = pos_tag(tokens)
        
        # Extract the part of speech tags
        pos_tags = [tag[1] for tag in pos_tags]
        
        return pos_tags