### Method Description:
    def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :param text: Text to be split
        :return: Split Text List
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """

### Solution Code:
    def split_sentences(self, text):
        pattern = self.generate_split_sentences_pattern()
        return self.split(pattern, text)

### Source Code:
    def split_sentences(text):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        last_sentence = sentences[-1]
        sentences = [sentence for sentence in sentences[:-1] if re.search(r'[^\w\s]', sentence)]
        sentences.append(last_sentence)
        return sentences

### Predicted Code:
    def split_sentences(self, text):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        last_sentence = sentences[-1]
        sentences = [sentence for sentence in sentences[:-1] if re.search(r'[^\w\s]', sentence)]
        sentences.append(last_sentence)
        return sentences

### Adaptation:
Total number: 1
### Raw Output:
```
    def split_sentences(self, text):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        last_sentence = sentences[-1]
        sentences = [sentence for sentence in sentences[:-1] if re.search(r'[^\w\s]', sentence)]
        sentences.append(last_sentence)
        return sentences
```

### Test Code:
class RegexUtilsTestSplitSentences(unittest.TestCase):
    def test_split_sentences_1(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa. Bbbb? Ccc!")
        self.assertEqual(res, ['Aaa', 'Bbbb', 'Ccc!'])

    def test_split_sentences_2(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa.Bbbb? Ccc!")
        self.assertEqual(res, ['Aaa.Bbbb', 'Ccc!'])

    def test_split_sentences_3(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa. bbbb? Ccc!")
        self.assertEqual(res, ['Aaa. bbbb', 'Ccc!'])

    def test_split_sentences_4(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa. bbbb, Ccc!")
        self.assertEqual(res, ['Aaa. bbbb, Ccc!'])

    def test_split_sentences_5(self):
        ru = RegexUtils()
        res = ru.split_sentences("Aaa, Bbbb? Ccc!")
        self.assertEqual(res, ['Aaa, Bbbb', 'Ccc!'])

### Test Output:
# 0 errors, 5 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_split_sentences_1: Lists differ: ['Aaa.', 'Bbbb?', 'Ccc!'] != ['Aaa', 'Bbbb', 'Ccc!']
#         test_split_sentences_2: Lists differ: ['Aaa.Bbbb?', 'Ccc!'] != ['Aaa.Bbbb', 'Ccc!']
#         test_split_sentences_3: Lists differ: ['Aaa.', 'bbbb?', 'Ccc!'] != ['Aaa. bbbb', 'Ccc!']
#         test_split_sentences_4: Lists differ: ['Aaa.', 'bbbb, Ccc!'] != ['Aaa. bbbb, Ccc!']
#         test_split_sentences_5: Lists differ: ['Aaa, Bbbb?', 'Ccc!'] != ['Aaa, Bbbb', 'Ccc!']


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: split, generate_split_sentences_pattern


