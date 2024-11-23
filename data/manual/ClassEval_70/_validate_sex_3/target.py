class PersonRequest:
    def _validate_sex(self, sex: str) -> None:
        """
        Validate the sex and set it to the validated sex or None if invalid.
        :param sex: str, the sex to validate
        """
        if sex not in ['Man', 'Woman', 'UGM']:
            sex = None
        self.sex = sex