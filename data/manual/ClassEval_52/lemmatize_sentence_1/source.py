class Lemmatization:
    def lemmatize_sentence(sentence):
        # Remove punctuations from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_tokens = pos_tag(tokens)
        
        # Lemmatize the words
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token, tag in tagged_tokens]
        
        return lemmatized_tokens