class CamelCaseMap:
    def __delitem__(self, key):
        """
        Delete the value corresponding to the key
        :param key:str
        :return:None
        """
        if key in self._data:
            del self._data[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the dictionary.")