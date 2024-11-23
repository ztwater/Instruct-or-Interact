class PersonRequest:
    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        if phoneNumber == "" or len(phoneNumber) != 11:
            return None
        else:
            return phoneNumber