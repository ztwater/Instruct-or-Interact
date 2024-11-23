class CamelCaseMap:
    def __delitem__(self, key):
        if key in self._data:
            del self._data[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the dictionary.")