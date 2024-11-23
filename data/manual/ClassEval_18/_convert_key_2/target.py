class CamelCaseMap:
    def _convert_key(self, key):
        words = key.split('_')
        camel_case = words[0] + ''.join(word.title() for word in words[1:])
        return camel_case