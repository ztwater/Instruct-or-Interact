class NLPDataProcessor:
    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        """
        stop_words = ['a', 'an', 'the']
        return stop_words