### Method Description:
    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """

### Solution Code:
    def precision(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)

### Source Code:
    def precision(true_positives, false_positives):
        if true_positives + false_positives == 0:
            return 0
        else:
            return true_positives / (true_positives + false_positives)

### Predicted Code:
    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_positives == 0:
            return 0
        else:
            return self.true_positives / (self.true_positives + self.false_positives)


### Adaptation:
Total number: 20
### Raw Output:
```python
class MetricsCalculator:  
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0

    def update(self, predicted_labels, true_labels):
        """
        Update the counts of true positives, false positives, false negatives, and true negatives
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        """
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == 1 and true_labels[i] == 1:
                self.true_positives += 1
            elif predicted_labels[i] == 1 and true_labels[i] == 0:
                self.false_positives += 1
            elif predicted_labels[i] == 0 and true_labels[i] == 1:
                self.false_negatives += 1
            elif predicted_labels[i] == 0 and true_labels[i] == 0:
                self.true_negatives += 1

    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_positives == 0:
            return 0
        else:
            return self.true_positives / (self.true_positives + self.false_positives)

    def recall(self, predicted_labels, true_labels):
        pass

    def f1_score(self, predicted_labels, true_labels):
        pass

    def accuracy(self, predicted_labels, true_labels):
        pass
```

### Test Code:
class MetricsCalculatorTestPrecision(unittest.TestCase):
    def test_precision_1(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_precision_2(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 1, 0], [1, 0, 0, 1])
        self.assertAlmostEqual(temp, 0.3333333333333333)

    def test_precision_3(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertAlmostEqual(temp, 0.6666666666666666)

    def test_precision_4(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 0], [1, 1, 0, 1])
        self.assertAlmostEqual(temp, 1.0)

    def test_precision_5(self):
        mc = MetricsCalculator()
        temp = mc.precision([1, 1, 0, 0], [1, 0, 1, 1])
        self.assertAlmostEqual(temp, 0.5)

    def test_precision_6(self):
        mc = MetricsCalculator()
        temp = mc.precision([0, 0, 0, 0], [1, 0, 1, 1])
        self.assertAlmostEqual(temp, 0.0)

### Test Output:
# 0 errors, 0 failures in 6 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.false_positives, self.true_positives
# method_dependencies: update


