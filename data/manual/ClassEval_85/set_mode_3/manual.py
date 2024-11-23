### Method Description:
    def set_mode(self, mode):
        """
        Get the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """

### Solution Code:
    def set_mode(self, mode):
        if mode in ['heat', 'cool']:
            self.mode = mode
        else:
            return False

### Source Code:
    def set_mode():
        mode = input("Enter the current work mode: ")
        return mode

### Predicted Code:
    def set_mode(self, mode):
        """
        Set the current work mode
        :param mode: str, working mode. only ['heat', 'cool']
        """
        self.mode = mode

### Adaptation:
Total number: 10
### Raw Output:
Here is the adapted method `set_mode` in the class context of `Thermostat`:

```
def set_mode(self, mode):
    """
    Set the current work mode
    :param mode: str, working mode. only ['heat', 'cool']
    """
    self.mode = mode
```

### Test Code:
class ThermostatTestSetMode(unittest.TestCase):
    def test_set_mode_1(self):
        t = Thermostat(20, 25, 'heat')
        t.set_mode('cool')
        self.assertEqual(t.get_mode(), 'cool')

    # use mode that not in ['heat', 'cool']
    def test_set_mode_2(self):
        t = Thermostat(20, 25, 'heat')
        self.assertFalse(t.set_mode('test'))

    def test_set_mode_3(self):
        t = Thermostat(20, 25, 'cool')
        t.set_mode('heat')
        self.assertEqual(t.get_mode(), 'heat')

    def test_set_mode_4(self):
        t = Thermostat(20, 25, 'test')
        t.set_mode('heat')
        self.assertEqual(t.get_mode(), 'heat')

    def test_set_mode_5(self):
        t = Thermostat(25, 25, 'cool')
        t.set_mode('heat')
        self.assertEqual(t.get_mode(), 'heat')

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.mode
# method_dependencies: 


