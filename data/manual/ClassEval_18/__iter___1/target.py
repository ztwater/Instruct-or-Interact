class CamelCaseMap:
    def __iter__(self):
        """
        Returning Iterateable Objects with Own Data
        :return: Iterator
        """
        return iter(self._data)