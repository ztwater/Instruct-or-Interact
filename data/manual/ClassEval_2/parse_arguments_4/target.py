class ArgumentParser:
    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and invoke _convert_type to stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        """
        arguments_list = command_string.split()

        for argument in arguments_list:
            if argument.startswith("--"):
                arg = argument[2:]
                if "=" in arg:
                    key, value = arg.split("=")
                else:
                    key = arg
                    value = True
                self.arguments[key] = self._convert_type(key, value)

            elif argument.startswith("-"):
                arg = argument[1:]
                value = arguments_list[arguments_list.index(argument) + 1]
                self.arguments[arg] = self._convert_type(arg, value)

        missing_args = self.required - set(self.arguments.keys())
        if missing_args:
            return False, missing_args
        else:
            return True, None
