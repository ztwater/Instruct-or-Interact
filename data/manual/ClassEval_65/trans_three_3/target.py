class NumberWordFormatter:
    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        ones = self.NUMBER
        tens = self.NUMBER_TEN
        teens = self.NUMBER_TEEN

        number_str = s

        hundreds_digit = int(number_str[0])
        tens_digit = int(number_str[1])
        ones_digit = int(number_str[2])

        hundreds_word = ones[hundreds_digit] + " HUNDRED" if hundreds_digit != 0 else ""
        tens_word = tens[tens_digit]
        ones_word = ones[ones_digit]

        if tens_digit == 1:
            tens_word = teens[ones_digit]
            ones_word = ""

        result = hundreds_word + " AND " + tens_word + " " + ones_word
        return result

