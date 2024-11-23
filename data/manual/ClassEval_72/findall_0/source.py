class RegexUtils:
    def findall(string, substring):
        matches = []
        start = 0
        while True:
            index = string.find(substring, start)
            if index == -1:
                break
            matches.append(string[index:index+len(substring)])
            start = index + 1
        return matches