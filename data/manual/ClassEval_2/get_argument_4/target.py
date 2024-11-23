class ArgumentParser:
    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        """
        if key in self.arguments:
            return self.arguments[key]
        else:
            return None