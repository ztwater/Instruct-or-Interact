class CamelCaseMap:
    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key:str
        :return:None
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map['first_name'] = 'John'
        >>> camelize_map.__delitem__('first_name')
        >>> flag = 'first_name' in camelize_map
        flag = False
        """
        if key in self._data:
            del self._data[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the dictionary.")