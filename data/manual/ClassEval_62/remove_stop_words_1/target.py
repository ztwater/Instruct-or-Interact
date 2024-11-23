class NLPDataProcessor:
    def remove_stop_words(self, string_list, stop_word_list):
        result = []
        for string in string_list:
            words = string.split()
            filtered_words = [word for word in words if word.lower() not in stop_word_list]
            result.append(filtered_words)
        return result