class ArgumentParser:
    def _convert_type(self, arg, value):
        for t in self.types.values():
            try:
                converted_value = t(value)
                return converted_value
            except ValueError:
                pass
        return value