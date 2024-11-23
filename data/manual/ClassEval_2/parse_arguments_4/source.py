class ArgumentParser:
    def parse_arguments(argument_string):
        arguments = {}
        arguments_list = argument_string.split()
    
        for argument in arguments_list:
            key_value = argument.split('=')
            key = key_value[0]
            value = key_value[1]
    
            arguments[key] = _convert_type(value)
    
        return arguments
    