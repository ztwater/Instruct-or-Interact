class NumberWordFormatter:
    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        def trans_two(s):
            if s[0] == '0':
                return self.NUMBER[int(s[1])]
            elif s[0] == '1':
                return self.NUMBER_TEEN[int(s[1])]
            else:
                return self.NUMBER_TEN[int(s[0])] + " " + self.NUMBER[int(s[1])]

        def trans_three(s):
            if s[0] == '0':
                return trans_two(s[1:])
            else:
                return self.NUMBER[int(s[0])] + " HUNDRED " + trans_two(s[1:])

        def parse_more(i):
            if i == 0:
                return ""
            elif i == 1:
                return "THOUSAND"
            else:
                return self.NUMBER[i] + " " + self.NUMBER_MORE[i]

        # Define a dictionary to map numbers to words
        words = {
            '0': 'ZERO',
            '1': 'ONE',
            '2': 'TWO',
            '3': 'THREE',
            '4': 'FOUR',
            '5': 'FIVE',
            '6': 'SIX',
            '7': 'SEVEN',
            '8': 'EIGHT',
            '9': 'NINE'
        }

        # Convert each digit in the string to its corresponding word
        result = []
        length = len(x)
        x = x[::-1]
        for i in range(length // 3 + 1):
            if i == length // 3 and length % 3 != 0:
                s = x[i * 3: length]
            else:
                s = x[i * 3: i * 3 + 3]

            if int(s) == 0:
                continue

            if len(s) == 3:
                result.append(trans_three(s))
            else:
                result.append(trans_two(s))

            result.append(parse_more(i))

        # Join the words together and return the result
        return ' '.join(result) + " ONLY"