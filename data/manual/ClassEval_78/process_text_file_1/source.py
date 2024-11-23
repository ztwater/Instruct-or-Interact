class SplitSentence:
    def process_text_file(text):
        sentences = text.split('. ')
        longest_sentence = max(sentences, key=lambda sentence: len(sentence.split()))
        num_words = len(longest_sentence.split())
        return num_words