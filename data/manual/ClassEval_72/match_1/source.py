class RegexUtils:
    def match(text, regex):
        if re.match(regex, text):
            return True
        else:
            return False