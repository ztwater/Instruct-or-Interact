class RegexUtils:
    def generate_email_pattern(self):
        # Regular expression pattern for email addresses
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        return pattern