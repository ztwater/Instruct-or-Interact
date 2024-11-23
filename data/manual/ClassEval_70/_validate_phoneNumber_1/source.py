class PersonRequest:
    def _validate_phoneNumber(phoneNumber):
        if phoneNumber == "" or len(phoneNumber) != 11:
            return None
        else:
            return phoneNumber