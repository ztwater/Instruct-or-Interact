### Method Description:
    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'
        """

### Solution Code:
    def remove_punctuation(self, sentence):
        return sentence.translate(str.maketrans('', '', string.punctuation))

### Source Code:
    def remove_punctuation(text):
        # Create a translation table to remove punctuation
        translator = str.maketrans("", "", string.punctuation)
        
        # Remove punctuation from the text using the translation table
        text_without_punctuation = text.translate(translator)
        
        return text_without_punctuation

### Predicted Code:
    def remove_punctuation(self, sentence):
        """
        Removes punctuation from the input text.
        :param sentence: a sentence str
        :return: str, sentence without any punctuation
        """
        # Create a translation table to remove punctuation
        translator = str.maketrans("", "", string.punctuation)
    
        # Remove punctuation from the sentence using the translation table
        sentence_without_punctuation = sentence.translate(translator)
    
        return sentence_without_punctuation

### Adaptation:
Total number: 7
### Raw Output:
```python
def remove_punctuation(self, sentence):
    """
    Removes punctuation from the input text.
    :param sentence: a sentence str
    :return: str, sentence without any punctuation
    """
    # Create a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation)

    # Remove punctuation from the sentence using the translation table
    sentence_without_punctuation = sentence.translate(translator)

    return sentence_without_punctuation
```

### Test Code:
class LemmatizationTestRemovePunctuation(unittest.TestCase):
    def test_remove_punctuation_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("I am running in a race.")
        expected = "I am running in a race"
        self.assertEqual(result, expected)

    def test_remove_punctuation_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("Until the beating, Cantanco's eyesight had been weak, but adequate.")
        expected = 'Until the beating Cantancos eyesight had been weak but adequate'
        self.assertEqual(result, expected)

    def test_remove_punctuation_3(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("The dog's barked at the mailman!!!")
        expected = 'The dogs barked at the mailman'
        self.assertEqual(result, expected)

    def test_remove_punctuation_4(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("He was running and eating at same time... ")
        expected = 'He was running and eating at same time '
        self.assertEqual(result, expected)

    def test_remove_punctuation_5(self):
        lemmatization = Lemmatization()
        result = lemmatization.remove_punctuation("Is this a test? I hope it is...")
        expected = 'Is this a test I hope it is'
        self.assertEqual(result, expected)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: string
# field_dependencies: 
# method_dependencies: 


