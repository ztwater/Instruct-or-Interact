### Method Description:
    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']
        """

### Solution Code:
    def lemmatize_sentence(self, sentence):
        lemmatized_words = []
        sentence = self.remove_punctuation(sentence)
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for word, tag in tagged_words:
            if tag.startswith('V'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='v')
            elif tag.startswith('J'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='a')
            elif tag.startswith('R'):
                lemmatized_word = self.lemmatizer.lemmatize(word, pos='r')
            else:
                lemmatized_word = self.lemmatizer.lemmatize(word)
            lemmatized_words.append(lemmatized_word)
        return lemmatized_words

### Source Code:
    def lemmatize_sentence(sentence):
        # Remove punctuations from the sentence
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_tokens = pos_tag(tokens)
        
        # Lemmatize the words
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token, tag in tagged_tokens]
        
        return lemmatized_tokens

### Predicted Code:
    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']
        """
        # Remove punctuations from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_tokens = pos_tag(tokens)
        
        # Lemmatize the words
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token, tag in tagged_tokens]
        
        return lemmatized_tokens

### Adaptation:
Total number: 12
### Raw Output:
```python
class Lemmatization:  
    """
    This is a class about Lemmatization, which utilizes the nltk library to perform lemmatization and part-of-speech tagging on sentences, as well as remove punctuation.
    """

    def __init__(self):
        """
        creates a WordNetLemmatizer object and stores it in the self.lemmatizer member variable.
        """
        self.lemmatizer = WordNetLemmatizer()


    def get_pos_tag(self, sentence):
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_tokens = pos_tag(tokens)
        
        return tagged_tokens


    def remove_punctuation(self, sentence):
        # Remove punctuations from the sentence
        return sentence.translate(str.maketrans('', '', string.punctuation))


    def lemmatize_sentence(self, sentence):
        """
        Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
        lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
        :param sentence: a sentence str
        :return: a list of words which have been lemmatized.
        >>> lemmatization = Lemmatization()
        >>> lemmatization.lemmatize_sentence("I am running in a race.")
        ['I', 'be', 'run', 'in', 'a', 'race']
        """
        # Remove punctuations from the sentence
        sentence = self.remove_punctuation(sentence)
        
        # Tokenize the sentence
        tokens = word_tokenize(sentence)
        
        # Mark the part of speech tag of each word
        tagged_tokens = pos_tag(tokens)
        
        # Lemmatize the words
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token, tag in tagged_tokens]
        
        return lemmatized_tokens
```

### Test Code:
class LemmatizationTestLemmatizeSentence(unittest.TestCase):
    def test_lemmatize_sentence_1(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("I am running in a race.")
        expected = ['I', 'be', 'run', 'in', 'a', 'race']
        self.assertEqual(result, expected)

    def test_lemmatize_sentence_2(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("Until the beating, Cantanco's eyesight had been weak, but adequate.")
        expected = ['Until', 'the', 'beating', 'Cantancos', 'eyesight', 'have', 'be', 'weak', 'but', 'adequate']
        self.assertEqual(result, expected)

    def test_lammatize_sentence_3(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("The dog's barked at the mailman.")
        expected = ['The', 'dog', 'bark', 'at', 'the', 'mailman']
        self.assertEqual(result, expected)

    def test_lemmatize_sentence_4(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("He was running and eating at same time. ")
        expected = ['He', 'be', 'run', 'and', 'eat', 'at', 'same', 'time']
        self.assertEqual(result, expected)

    def test_lemmatize_sentence_5(self):
        lemmatization = Lemmatization()
        result = lemmatization.lemmatize_sentence("I was taking a ride in the car.")
        expected = ['I', 'be', 'take', 'a', 'ride', 'in', 'the', 'car']
        self.assertEqual(result, expected)

### Test Output:
# 5 errors, 0 failures in 5 runs.
# errors:
#     LookupError:
#         test_lammatize_sentence_3: 
#         test_lemmatize_sentence_1: 
#         test_lemmatize_sentence_2: 
#         test_lemmatize_sentence_4: 
#         test_lemmatize_sentence_5: 
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.lemmatizer
# method_dependencies: remove_punctuation


