### Method Description:
    def get_pos_tag(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word.
        :param sentence: a sentence str
        :return: list, part of speech tag of each word in the sentence.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.get_pos_tag("I am running in a race.")
        ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
        """

### Solution Code:
    def get_pos_tag(self, sentence):
        pos_tags = []
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for tagged_word in tagged_words:
            pos_tags.append(tagged_word[1])
        return pos_tags

### Source Code:
    def get_pos_tag(sentence):
        # Remove punctuations
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark part of speech tag for each word
        pos_tags = pos_tag(tokens)
        
        return pos_tags

### Predicted Code:
    def get_pos_tag(self, sentence):
        sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        return [tag for word, tag in pos_tags]

### Adaptation:
Total number: 10
### Raw Output:
```python
    def get_pos_tag(self, sentence):
        sentence = self.remove_punctuation(sentence)
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        return [tag for word, tag in pos_tags]
```

### Test Code:
class LemmatizationTestGetPosTag(unittest.TestCase):
    def test_get_pos_tag_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("I am running in a race.")
        expected = ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
        self.assertEqual(result, expected)

    def test_get_pos_tag_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("Cantanco's eyesight had been weak, but adequate.")
        expected = ['NNP', 'NN', 'VBD', 'VBN', 'JJ', 'CC', 'JJ']
        self.assertEqual(result, expected)

    def test_get_pos_tag_3(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("The dog's barked at the mailman.")
        expected = ['DT', 'NNS', 'VBD', 'IN', 'DT', 'NN']
        self.assertEqual(result, expected)

    def test_get_pos_tag_4(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("He was running and eating at same time. ")
        expected = ['PRP', 'VBD', 'VBG', 'CC', 'VBG', 'IN', 'JJ', 'NN']
        self.assertEqual(result, expected)

    def test_get_pos_tag_5(self):
        lemmatization = Lemmatization()
        result = lemmatization.get_pos_tag("I was taking a ride in the car.")
        expected = ['PRP', 'VBD', 'VBG', 'DT', 'NN', 'IN', 'DT', 'NN']
        self.assertEqual(result, expected)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: remove_punctuation


