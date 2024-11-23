class Lemmatization:
    def get_pos_tag(self, sentence):
        sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        return [tag for word, tag in pos_tags]