class ArgumentParser:
    def _convert_type(self, arg, value):
        if arg in self.types:
            try:
                converted_value = self.types[arg](value)
                return converted_value
            except ValueError:
                pass
        return value