### Method Description:
    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return:None
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323

        """

### Solution Code:
    def display(self, key, value):
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value)

### Source Code:
    def display(chord, tune):
        print("Normal Guitar Playing -- Chord: %s, Play Tune: %s." % (chord, tune))

### Predicted Code:
    def display(self, key, value):
        print("Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value))

### Adaptation:
Total number: 6
### Raw Output:
```python
def display(self, key, value):
    print("Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value))
```

### Test Code:
class AutomaticGuitarSimulatorTestDisplay(unittest.TestCase):
    def test_display_1(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323")
        play_list = context.interpret()
        str = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
        self.assertEqual(str, "Normal Guitar Playing -- Chord: C, Play Tune: 53231323")

    def test_display_2(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323")
        play_list = context.interpret()
        str = context.display(play_list[1]['Chord'], play_list[1]['Tune'])
        self.assertEqual(str, "Normal Guitar Playing -- Chord: Em, Play Tune: 43231323")

    def test_display_3(self):
        context = AutomaticGuitarSimulator("F43231323 G63231323")
        play_list = context.interpret()
        str = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
        self.assertEqual(str, "Normal Guitar Playing -- Chord: F, Play Tune: 43231323")

    def test_display_4(self):
        context = AutomaticGuitarSimulator("F43231323 G63231323")
        play_list = context.interpret()
        str = context.display(play_list[1]['Chord'], play_list[1]['Tune'])
        self.assertEqual(str, "Normal Guitar Playing -- Chord: G, Play Tune: 63231323")

    def test_display_5(self):
        context = AutomaticGuitarSimulator("")
        str = context.display('', '')
        self.assertEqual(str, "Normal Guitar Playing -- Chord: , Play Tune: ")

### Test Output:
# 0 errors, 5 failures in 5 runs.
# errors:
# failures:
#     AssertionError:
#         test_display_1: None != 'Normal Guitar Playing -- Chord: C, Play Tune: 53231323'
#         test_display_2: None != 'Normal Guitar Playing -- Chord: Em, Play Tune: 43231323'
#         test_display_3: None != 'Normal Guitar Playing -- Chord: F, Play Tune: 43231323'
#         test_display_4: None != 'Normal Guitar Playing -- Chord: G, Play Tune: 63231323'
#         test_display_5: None != 'Normal Guitar Playing -- Chord: , Play Tune: '


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: 


