### Method Description:
    def get_target_temperature(self):
        """
        Get the target temperature of an instance of the Thermostat class.
        :return self.current_temperature: int
        >>> thermostat.get_target_temperature()
        37.5
        """

### Solution Code:
    def get_target_temperature(self):
        return self.target_temperature

### Source Code:
    def get_target_temperature(self):
        return self.target_temperature

### Predicted Code:
    def get_target_temperature(self):
        """
        Get the target temperature of an instance of the Thermostat class.
        :return self.target_temperature: float
        """
        return self.target_temperature

### Adaptation:
Total number: 1
### Raw Output:
```
    def get_target_temperature(self):
        """
        Get the target temperature of an instance of the Thermostat class.
        :return self.target_temperature: float
        """
        return self.target_temperature
```

### Test Code:
class ThermostatTestGetTargetTemperature(unittest.TestCase):
    def test_get_target_temperature_1(self):
        t = Thermostat(20, 25, 'heat')
        self.assertEqual(t.get_target_temperature(), 25)

    def test_get_target_temperature_2(self):
        t = Thermostat(20, 25, 'cool')
        self.assertEqual(t.get_target_temperature(), 25)

    def test_get_target_temperature_3(self):
        t = Thermostat(20, 25, 'test')
        self.assertEqual(t.get_target_temperature(), 25)

    def test_get_target_temperature_4(self):
        t = Thermostat(25, 25, 'cool')
        self.assertEqual(t.get_target_temperature(), 25)

    def test_get_target_temperature_5(self):
        t = Thermostat(25, 25, 'heat')
        self.assertEqual(t.get_target_temperature(), 25)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.target_temperature
# method_dependencies: 


