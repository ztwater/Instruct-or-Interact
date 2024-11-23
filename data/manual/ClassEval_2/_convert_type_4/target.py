class ArgumentParser:
    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value oherwise
        """
        for key, arg_type in self.types.items():
            if key == arg:
                try:
                    converted_value = arg_type(value)
                    return converted_value
                except ValueError:
                    pass
        return value