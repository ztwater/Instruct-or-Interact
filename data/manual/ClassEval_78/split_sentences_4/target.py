class SplitSentence:
    def split_sentences(self, sentences_string):
        sentences = []
        current_sentence = ""
        for char in sentences_string:
            current_sentence += char
            if char in ['.', '?'] and current_sentence.strip()[-3:] != "Mr.":
                sentences.append(current_sentence.strip())
                current_sentence = ""
        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        return sentences