class ArgumentParser:
    def parse_arguments(self, command_string):
        """
        Parses the given command line argument string and invoke _convert_type to stores the parsed result in specific type in the arguments dictionary.
        Checks for missing required arguments, if any, and returns False with the missing argument names, otherwise returns True.
        :param command_string: str, command line argument string, formatted like "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) if parsing is successful, (False, missing_args) if parsing fails,
            where missing_args is a set of the missing argument names which are str.
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
        arguments_list = command_string.split()

        missing_args = set()

        for argument in arguments_list:
            if argument.startswith("--"):
                arg_name, arg_value = argument[2:].split("=")
            elif argument.startswith("-"):
                arg_name = argument[1:]
                if arguments_list.index(argument) + 1 < len(arguments_list) and not arguments_list[arguments_list.index(argument) + 1].startswith("-"):
                    arg_value = arguments_list[arguments_list.index(argument) + 1]
                else:
                    arg_value = True
            else:
                continue

            if arg_name in self.arguments:
                self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
            else:
                missing_args.add(arg_name)

        if missing_args:
            return False, missing_args
        else:
            return True, None