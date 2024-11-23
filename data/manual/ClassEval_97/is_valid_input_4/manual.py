### Method Description:
    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """

### Solution Code:
    def is_valid_input(self, textnum):

        textnum = textnum.replace('-', ' ')

        for word in textnum.split():
            if word in self.ordinal_words:
                continue
            else:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in self.numwords:
                    return False

        return True

### Source Code:
    def is_valid_input(text):
        valid_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        
        words = text.split()
        for word in words:
            if word.lower() not in valid_words:
                return False
        
        return True

### Predicted Code:
    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        valid_words = self.units + self.tens + self.scales
        
        words = textnum.split()
        for word in words:
            if word.lower() not in valid_words:
                return False
        
        return True

### Adaptation:
Total number: 28
### Raw Output:
```
    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        valid_words = self.units + self.tens + self.scales
        
        words = textnum.split()
        for word in words:
            if word.lower() not in valid_words:
                return False
        
        return True
```

### Test Code:
class Words2NumbersTestIsValidInput(unittest.TestCase):
    def test_is_valid_input(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("twenty-five thousand three hundred and forty-two"))

    def test_is_valid_input2(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("second hundred and third"))

    def test_is_valid_input3(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("twenty-fifth thousand three hundred and forty-second"))

    def test_is_valid_input4(self):
        w2n = Words2Numbers()
        self.assertFalse(w2n.is_valid_input("eleventy thousand and five"))

    def test_is_valid_input5(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("seventy two thousand and hundred eleven"))

    def test_is_valid_input6(self):
        w2n = Words2Numbers()
        self.assertTrue(w2n.is_valid_input("fifteenth hundred"))

### Test Output:
# 0 errors, 5 failures in 6 runs.
# errors:
# failures:
#     AssertionError:
#         test_is_valid_input: False is not true
#         test_is_valid_input2: False is not true
#         test_is_valid_input3: False is not true
#         test_is_valid_input5: False is not true
#         test_is_valid_input6: False is not true


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.numwords, self.ordinal_endings, self.ordinal_words
# method_dependencies: 


