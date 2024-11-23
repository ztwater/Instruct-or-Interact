class ArgumentParser:
    def _convert_type(self, arg, value):
        for t in self.types:
            try:
                converted_value = self.types[t](value)
                return converted_value
            except ValueError:
                pass
        return value