class SplitSentence:
    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        sentences = sentences_string.split('. ')
        longest_sentence = max(sentences, key=lambda sentence: len(sentence.split()))
        num_words = len(longest_sentence.split())
        return num_words