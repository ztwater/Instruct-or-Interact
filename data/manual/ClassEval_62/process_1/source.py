class NLPDataProcessor:
    def process(strings):
        stop_words = ['a', 'an', 'the']
        result = []
        
        for string in strings:
            words = string.split()
            filtered_words = [word for word in words if word.lower() not in stop_words]
            result.append(' '.join(filtered_words))
        
        return result