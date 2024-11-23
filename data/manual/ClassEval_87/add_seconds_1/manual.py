### Method Description:
    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """

### Solution Code:
    def add_seconds(self, seconds):
        new_datetime = self.datetime + datetime.timedelta(seconds=seconds)
        format = "%H:%M:%S"
        return new_datetime.strftime(format)

### Source Code:
    def add_seconds(seconds):
        current_time = datetime.datetime.now()
        new_time = current_time + datetime.timedelta(seconds=seconds)
        return new_time

### Predicted Code:
    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
        current_time = self.datetime
        new_time = current_time + datetime.timedelta(seconds=seconds)
        return new_time.strftime("%H:%M:%S")

### Adaptation:
Total number: 8
### Raw Output:
```python
class TimeUtils:
    def __init__(self):
        self.datetime = datetime.datetime.now()

    def add_seconds(self, seconds):
        """
        Add the specified number of seconds to the current time
        :param seconds: int, number of seconds to add
        :return: string, time after adding the specified number of seconds in the format '%H:%M:%S'
        >>> timeutils.add_seconds(600)
        "19:29:22"
        """
        current_time = self.datetime
        new_time = current_time + datetime.timedelta(seconds=seconds)
        return new_time.strftime("%H:%M:%S")
```

### Test Code:
class TimeUtilsTestAddSeconds(unittest.TestCase):
    def test_add_seconds_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(600),
                         (timeutils.datetime + datetime.timedelta(seconds=600)).strftime("%H:%M:%S"))

    def test_add_seconds_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(500),
                         (timeutils.datetime + datetime.timedelta(seconds=500)).strftime("%H:%M:%S"))

    def test_add_seconds_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(400),
                         (timeutils.datetime + datetime.timedelta(seconds=400)).strftime("%H:%M:%S"))

    def test_add_seconds_4(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(300),
                         (timeutils.datetime + datetime.timedelta(seconds=300)).strftime("%H:%M:%S"))

    def test_add_seconds_5(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.add_seconds(200),
                         (timeutils.datetime + datetime.timedelta(seconds=200)).strftime("%H:%M:%S"))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: datetime, time
# field_dependencies: self.datetime
# method_dependencies: 


