class CamelCaseMap:
    def __delitem__(self, key):
        if key in self:
            del self[key]
        else:
            raise KeyError(f"Key '{key}' does not exist in the dictionary.")