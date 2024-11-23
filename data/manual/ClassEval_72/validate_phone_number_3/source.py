class RegexUtils:
    def validate_phone_number(phone_number):
        # Remove any non-digit characters from the phone number
        phone_number = ''.join(filter(str.isdigit, phone_number))
    
        # Check if the phone number has 10 digits
        if len(phone_number) == 10:
            return True
        else:
            return False