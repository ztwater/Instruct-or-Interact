class CamelCaseMap:
    def _to_camel_case(self):
        """
        convert key string into camel case
        :param self: reference to the instance of CamelCaseMap
        :return: str, converted key string
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
        words = self.split('_')
        camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        return camel_case
