class SplitSentence:
    def process_text_file(self, sentences_string):
        sentences = re.split('[.?!]', sentences_string)
        longest_sentence = max(sentences, key=lambda sentence: len(sentence.split()))
        num_words = len(longest_sentence.split())
        return num_words