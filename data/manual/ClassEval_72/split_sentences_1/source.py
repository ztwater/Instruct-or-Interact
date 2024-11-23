class RegexUtils:
    def split_sentences(text):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        last_sentence = sentences[-1]
        sentences = [sentence for sentence in sentences[:-1] if re.search(r'[^\w\s]', sentence)]
        sentences.append(last_sentence)
        return sentences