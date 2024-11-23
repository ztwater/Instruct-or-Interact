class RegexUtils:
    def match(self, pattern, text):
        if re.match(pattern, text):
            return True
        else:
            return False