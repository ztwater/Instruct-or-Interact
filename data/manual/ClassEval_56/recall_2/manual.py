### Method Description:
    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """

### Solution Code:
    def recall(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)

### Source Code:
    def recall(true_positives, false_negatives):
        recall = true_positives / (true_positives + false_negatives)
        return recall

### Predicted Code:
    def recall(self, predicted_labels, true_labels):
        true_positives = 0
        false_negatives = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                true_positives += 1
            elif predicted == 0 and true == 1:
                false_negatives += 1
        recall = true_positives / (true_positives + false_negatives)
        return recall

### Adaptation:
Total number: 6
### Raw Output:
To adapt the provided method `recall` to the class context of `MetricsCalculator`, we need to make the following changes:

1. Move the method inside the `MetricsCalculator` class.
2. Modify the method signature to include the `self` parameter.
3. Replace the `true_positives` and `false_negatives` parameters with the corresponding instance variables `self.true_positives` and `self.false_negatives`.

Here is the adapted `recall` method:

```python
def recall(self, predicted_labels, true_labels):
    true_positives = 0
    false_negatives = 0
    for predicted, true in zip(predicted_labels, true_labels):
        if predicted == 1 and true == 1:
            true_positives += 1
        elif predicted == 0 and true == 1:
            false_negatives += 1
    recall = true_positives / (true_positives + false_negatives)
    return recall
```

### Test Code:
class MetricsCalculatorTestRecall(unittest.TestCase):
    def test_recall_1(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_recall_2(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 1, 0], [1, 0, 0, 1])
        self.assertEqual(temp, 0.5)

    def test_recall_3(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 1], [1, 0, 0, 1])
        self.assertEqual(temp, 1.0)

    def test_recall_4(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 0], [1, 1, 0, 1])
        self.assertAlmostEqual(temp, 0.6666666666666666)

    def test_recall_5(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 0], [1, 0, 1, 1])
        self.assertAlmostEqual(temp, 0.3333333333333333)

    def test_recall_6(self):
        mc = MetricsCalculator()
        temp = mc.recall([1, 1, 0, 0], [0, 0, 0, 0])
        self.assertEqual(temp, 0.0)

### Test Output:
# 1 errors, 0 failures in 6 runs.
# errors:
#     ZeroDivisionError:
#         test_recall_6: division by zero
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.false_negatives, self.true_positives
# method_dependencies: update


