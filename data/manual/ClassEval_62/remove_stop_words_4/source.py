class NLPDataProcessor:
    def remove_stop_words(strings):
        stop_words = ['the', 'and', 'is', 'in', 'it', 'to']  # example list of stop words
        result = []
        for string in strings:
            words = string.split()
            filtered_words = [word for word in words if word.lower() not in stop_words]
            result.append(' '.join(filtered_words))
        return result