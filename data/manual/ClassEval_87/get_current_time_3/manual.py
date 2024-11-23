### Method Description:
    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        >>> timeutils = TimeUtils()
        >>> timeutils.get_current_time()
        "19:19:22"
        """

### Solution Code:
    def get_current_time(self):
        format = "%H:%M:%S"
        return self.datetime.strftime(format)

### Source Code:
    def get_current_time():
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        return current_time

### Predicted Code:
    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        """
        current_time = self.datetime.strftime('%H:%M:%S')
        return current_time

### Adaptation:
Total number: 5
### Raw Output:
```
    def get_current_time(self):
        """
        Return the current time in the format of '%H:%M:%S'
        :return: string
        """
        current_time = self.datetime.strftime('%H:%M:%S')
        return current_time
```

### Test Code:
class TimeUtilsTestGetCurrentTime(unittest.TestCase):
    def test_get_current_time_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

    def test_get_current_time_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

    def test_get_current_time_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

    def test_get_current_time_4(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

    def test_get_current_time_5(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_time(), timeutils.datetime.strftime("%H:%M:%S"))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: datetime, time
# field_dependencies: self.datetime
# method_dependencies: 


