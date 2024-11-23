class Lemmatization:
    def get_pos_tag(sentence):
        # Remove punctuations
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark part of speech tag for each word
        pos_tags = pos_tag(tokens)
        
        return pos_tags