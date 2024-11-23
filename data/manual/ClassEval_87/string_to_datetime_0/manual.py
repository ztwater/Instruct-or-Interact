### Method Description:
    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """

### Solution Code:
    def string_to_datetime(self, string):
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

### Source Code:
    def string_to_datetime(time_string):
        datetime_obj = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        return datetime_obj

### Predicted Code:
    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
        datetime_obj = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
        return datetime_obj

### Adaptation:
Total number: 5
### Raw Output:
```
    def string_to_datetime(self, string):
        """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
        datetime_obj = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
        return datetime_obj
```

### Test Code:
class TimeUtilsTestStringToDatetime(unittest.TestCase):
    def test_string_to_datetime_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-18 1:1:1'), datetime.datetime(2001, 7, 18, 1, 1, 1))

    def test_string_to_datetime_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-17 1:1:1'), datetime.datetime(2001, 7, 17, 1, 1, 1))

    def test_string_to_datetime_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-16 1:1:1'), datetime.datetime(2001, 7, 16, 1, 1, 1))

    def test_string_to_datetime_4(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-15 1:1:1'), datetime.datetime(2001, 7, 15, 1, 1, 1))

    def test_string_to_datetime_5(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.string_to_datetime('2001-7-14 1:1:1'), datetime.datetime(2001, 7, 14, 1, 1, 1))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: datetime, time
# field_dependencies: 
# method_dependencies: 


