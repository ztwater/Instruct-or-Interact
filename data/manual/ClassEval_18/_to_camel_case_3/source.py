class CamelCaseMap:
    def _to_camel_case(key):
        words = key.split('_')
        camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        return camel_case