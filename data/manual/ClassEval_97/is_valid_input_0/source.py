class Words2Numbers:
    def is_valid_input(text):
        valid_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        
        words = text.split()
        for word in words:
            if word.lower() not in valid_words:
                return False
        
        return True