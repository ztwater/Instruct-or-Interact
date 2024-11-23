### Method Description:
    def datetime_to_string(self, datetime):
        """
        Convert a datetime instance to a string
        :param datetime: the datetime instance to convert
        :return: string, converted time string
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """

### Solution Code:
    def datetime_to_string(self, datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")

### Source Code:
    def datetime_to_string(dt):
        return dt.strftime("%Y-%m-%d %H:%M:%S")

### Predicted Code:
    def datetime_to_string(self, datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")

### Adaptation:
Total number: 3
### Raw Output:
```python
    def datetime_to_string(self, datetime):
        return datetime.strftime("%Y-%m-%d %H:%M:%S")
```

### Test Code:
class TimeUtilsTestDatetimeToString(unittest.TestCase):
    def test_datetime_to_string_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

    def test_datetime_to_string_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

    def test_datetime_to_string_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

    def test_datetime_to_string_4(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

    def test_datetime_to_string_5(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.datetime_to_string(timeutils.datetime),
                         timeutils.datetime.strftime("%Y-%m-%d %H:%M:%S"))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: datetime, time
# field_dependencies: 
# method_dependencies: 


