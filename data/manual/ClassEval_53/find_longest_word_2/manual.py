### Method Description:
    def find_longest_word(self, sentence):
        """
        Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
        Words are strictly case sensitive.
        :param sentence: a sentence str
        :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """

### Solution Code:
    def find_longest_word(self, sentence):
        longest_word = ""
        sentence = sentence.lower()
        sentence = re.sub('[%s]' % re.escape(string.punctuation), '', sentence)
        sentence = re.split(' ', sentence)
        for word in sentence:
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
        return longest_word

### Source Code:
    def find_longest_word(sentence, word_list):
        # Remove punctuation marks
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Split sentence into a list of words
        words = sentence.split()
        
        # Find the longest word that is in the word_list
        longest_word = ''
        for word in words:
            if word in word_list and len(word) > len(longest_word):
                longest_word = word
        
        return longest_word

### Predicted Code:
    def find_longest_word(self, sentence):
        # Remove punctuation marks
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Split sentence into a list of words
        words = sentence.split()
        
        # Find the longest word that is in the self.word_list
        longest_word = ''
        for word in words:
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
        
        return longest_word

### Adaptation:
Total number: 5
### Raw Output:
```python
    def find_longest_word(self, sentence):
        # Remove punctuation marks
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Split sentence into a list of words
        words = sentence.split()
        
        # Find the longest word that is in the self.word_list
        longest_word = ''
        for word in words:
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
        
        return longest_word
```

### Test Code:
class LongestWordTestFindLongestWord(unittest.TestCase):
    def test_find_longest_word_1(self):
        longestWord = LongestWord()
        longestWord.add_word("a")
        sentence = 'I am a student.'
        self.assertEqual('a', longestWord.find_longest_word(sentence))

    def test_find_longest_word_2(self):
        longestWord = LongestWord()
        sentence = 'I am a student.'
        self.assertEqual('', longestWord.find_longest_word(sentence))

    def test_find_longest_word_3(self):
        longestWord = LongestWord()
        longestWord.add_word("student")
        sentence = 'I am a student.'
        self.assertEqual('student', longestWord.find_longest_word(sentence))

    def test_find_longest_word_4(self):
        longestWord = LongestWord()
        longestWord.add_word("apple")
        sentence = 'Apple is red.'
        self.assertEqual('apple', longestWord.find_longest_word(sentence))

    def test_find_longest_word_5(self):
        longestWord = LongestWord()
        longestWord.add_word("apple")
        longestWord.add_word("red")
        sentence = 'Apple is red.'
        self.assertEqual('apple', longestWord.find_longest_word(sentence))

### Test Output:
# 0 errors, 2 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_find_longest_word_4: 'apple' != ''
#         test_find_longest_word_5: 'apple' != 'red'


### Dependencies:
# lib_dependencies: re, string
# field_dependencies: self.word_list
# method_dependencies: 


