class ArgumentParser:
    def _convert_type(self, value):
        for t in self.types:
            try:
                converted_value = t(value)
                return converted_value
            except ValueError:
                pass
        return value