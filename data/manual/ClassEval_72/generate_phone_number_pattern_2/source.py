class RegexUtils:
    def generate_phone_number_pattern():
        # Regular expression pattern for phone numbers
        pattern = r'^\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$'
        
        return pattern