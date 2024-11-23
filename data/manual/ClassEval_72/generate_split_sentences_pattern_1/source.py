class RegexUtils:
    def generate_split_sentences_pattern(sentence1, sentence2):
        # Get the middle characters of the first sentence
        middle1 = sentence1[len(sentence1) // 2]
        
        # Get the middle characters of the second sentence
        middle2 = sentence2[len(sentence2) // 2]
        
        # Generate the regular expression pattern
        pattern = f"{middle1}.{middle2}"
        
        return pattern