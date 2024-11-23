class CamelCaseMap:
    def __setitem__(self, key, value):
        """
        Set the value corresponding to the key to the specified value
        :param key:str
        :param value:str, the specified value
        :return:None
        """
        self._data[self._to_camel_case(key)] = value