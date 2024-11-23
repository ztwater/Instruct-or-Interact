### Method Description:
    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """

### Solution Code:
    def add_word(self, word):
        self.word_list.append(word)

### Source Code:
    def add_word(self, word):
        self.word_list.append(word)

### Predicted Code:
    def add_word(self, word):
        """
        Append the input word into self.word_list.
        :param word: str, input word
        """
        self.word_list.append(word)

### Adaptation:
Total number: 1
### Raw Output:
### Adapted Method
```
    def add_word(self, word):
        """
        Append the input word into self.word_list.
        :param word: str, input word
        """
        self.word_list.append(word)
```

### Test Code:
class LongestWordTestAddWord(unittest.TestCase):
    def test_add_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        self.assertEqual(['hello'], longestWord.word_list)

    def test_add_word_2(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        self.assertEqual(['hello', 'world'], longestWord.word_list)

    def test_add_word_3(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        longestWord.add_word("!")
        self.assertEqual(['hello', 'world', '!'], longestWord.word_list)

    def test_add_word_4(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        longestWord.add_word("!")
        longestWord.add_word("!")
        self.assertEqual(['hello', 'world', '!', '!'], longestWord.word_list)

    def test_add_word_5(self):
        longestWord = LongestWord()
        longestWord.add_word("hello")
        longestWord.add_word("world")
        longestWord.add_word("!")
        longestWord.add_word("!")
        longestWord.add_word("!")
        self.assertEqual(['hello', 'world', '!', '!', '!'], longestWord.word_list)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.word_list
# method_dependencies: 


