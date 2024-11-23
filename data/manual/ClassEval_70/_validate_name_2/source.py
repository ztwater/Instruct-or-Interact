class PersonRequest:
    def _validate_name(name):
        if name == "" or len(name) > 33:
            return None
        else:
            return name