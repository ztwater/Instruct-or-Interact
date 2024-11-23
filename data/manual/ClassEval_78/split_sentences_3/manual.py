### Method Description:
    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """

### Solution Code:
    def split_sentences(self, sentences_string):
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sentences_string)
        return sentences

### Source Code:
    def split_sentences(string):
        sentences = []
        current_sentence = ""
        for char in string:
            current_sentence += char
            if char in ['.', '?'] and current_sentence.strip()[-3:] != "Mr.":
                sentences.append(current_sentence.strip())
                current_sentence = ""
        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        return sentences

### Predicted Code:
    def split_sentences(self, sentences_string):
        sentences = []
        current_sentence = ""
        for char in sentences_string:
            current_sentence += char
            if char in ['.', '?'] and current_sentence.strip()[-3:] != "Mr.":
                sentences.append(current_sentence.strip())
                current_sentence = ""
        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        return sentences

### Adaptation:
Total number: 3
### Raw Output:
Here is the adapted method `split_sentences` in the context of the `SplitSentence` class:

```
class SplitSentence:  
    """
    The class allows to split sentences, count words in a sentence, and process a text file to find the maximum word count.
    """

    def split_sentences(self, sentences_string):
        sentences = []
        current_sentence = ""
        for char in sentences_string:
            current_sentence += char
            if char in ['.', '?'] and current_sentence.strip()[-3:] != "Mr.":
                sentences.append(current_sentence.strip())
                current_sentence = ""
        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        return sentences
```

### Test Code:
class SplitSentenceTestSplitSentences(unittest.TestCase):
    def test_split_sentences_1(self):
        ss = SplitSentence()
        lst = ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?'])

    def test_split_sentences_2(self):
        ss = SplitSentence()
        lst = ss.split_sentences("Who is Mr. Smith? He is a teacher.")
        self.assertEqual(lst, ['Who is Mr. Smith?', 'He is a teacher.'])

    def test_split_sentences_3(self):
        ss = SplitSentence()
        lst = ss.split_sentences("Who is A.B.C.? He is a teacher.")
        self.assertEqual(lst, ['Who is A.B.C.?', 'He is a teacher.'])

    def test_split_sentences_4(self):
        ss = SplitSentence()
        lst = ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc.")
        self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.'])

    def test_split_sentences_5(self):
        ss = SplitSentence()
        lst = ss.split_sentences("aaa aaaa. bb bbbb bbb?")
        self.assertEqual(lst, ['aaa aaaa.', 'bb bbbb bbb?'])

### Test Output:
# 0 errors, 1 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_split_sentences_3: Lists differ: ['Who is A.', 'B.', 'C.', '?', 'He is a teacher.'] != ['Who is A.B.C.?', 'He is a teacher.']


### Dependencies:
# lib_dependencies: re
# field_dependencies: 
# method_dependencies: 


