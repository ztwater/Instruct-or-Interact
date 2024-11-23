class RegexUtils:
    def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :param text: Text to be split
        :return: Split Text List
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
        sentences = re.split(r'(?<=[.!?])\s+', text)
        last_sentence = sentences[-1]
        sentences = [sentence for sentence in sentences[:-1] if re.search(r'[^\w\s]', sentence)]
        sentences.append(last_sentence)
        return sentences