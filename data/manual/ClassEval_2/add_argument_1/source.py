class ArgumentParser:
    def add_argument(self, argument_type, is_required):
        self.types.append(argument_type)
        self.required.append(is_required)