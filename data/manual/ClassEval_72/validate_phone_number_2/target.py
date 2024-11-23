class RegexUtils:
    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid
        :param phone_number: Phone number to be verified
        :return: True or False, indicating whether the phone number is valid
        >>> ru = RegexUtils()
        >>> ru.validate_phone_number("123-456-7890")
        True
        """
        # Remove any non-digit characters from the phone number
        phone_number = ''.join(filter(str.isdigit, phone_number))

        # Check if the phone number has 10 digits
        if len(phone_number) == 10:
            return True
        else:
            return False