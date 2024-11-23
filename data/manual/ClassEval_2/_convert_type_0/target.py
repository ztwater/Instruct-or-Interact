class ArgumentParser:
    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param arg: str, the argument name
        :param value: str, the input value in command line
        :return: corresponding value in self.types if converted successfully, or the input value otherwise
        """
        if arg in self.types:
            try:
                converted_value = self.types[arg](value)
                return converted_value
            except ValueError:
                pass
        return value