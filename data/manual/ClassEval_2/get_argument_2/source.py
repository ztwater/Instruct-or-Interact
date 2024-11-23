class ArgumentParser:
    def get_argument(arguments, argument_name):
        if argument_name in arguments:
            return arguments[argument_name]
        else:
            return None