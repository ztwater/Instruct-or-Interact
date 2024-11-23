class CamelCaseMap:
    def __delitem__(self, key):
        converted_key = self._convert_key(key)
        if converted_key in self._data:
            del self._data[converted_key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the dictionary.")