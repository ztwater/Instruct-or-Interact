class PersonRequest:
    def _validate_name(self, name: str) -> str:
        if name == "" or len(name) > 33:
            return None
        else:
            return name