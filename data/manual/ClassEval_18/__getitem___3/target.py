class CamelCaseMap:
    def __getitem__(self, key):
        """
        Return the value corresponding to the key
        :param key:str
        :return:str,the value corresponding to the key
        """
        camel_case_key = self._convert_key(key)
        return self._data[camel_case_key]