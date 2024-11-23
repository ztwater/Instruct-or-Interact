class NLPDataProcessor:
    def process(self, string_list):
        stop_words = ['a', 'an', 'the']
        result = []
        
        for string in string_list:
            words = string.split()
            filtered_words = [word for word in words if word.lower() not in stop_words]
            result.append(filtered_words)
        
        return result