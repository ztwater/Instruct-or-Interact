### Method Description:
    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        >>> timeutils.get_current_date()
        "2023-06-14"
        """

### Solution Code:
    def get_current_date(self):
        format = "%Y-%m-%d"
        return self.datetime.strftime(format)

### Source Code:
    def get_current_date():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return current_date

### Predicted Code:
    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        """
        current_date = self.datetime.strftime("%Y-%m-%d")
        return current_date

### Adaptation:
Total number: 5
### Raw Output:
Here is the adapted method `get_current_date` in the context of the `TimeUtils` class:

```python
    def get_current_date(self):
        """
        Return the current date in the format of "%Y-%m-%d"
        :return: string
        """
        current_date = self.datetime.strftime("%Y-%m-%d")
        return current_date
```
The `self.datetime` attribute is used to get the current datetime in the `TimeUtils` class. By calling the `strftime` method on `self.datetime` with the format `"%Y-%m-%d"`, we can obtain the current date in the desired format.

### Test Code:
class TimeUtilsTestGetCurrentDate(unittest.TestCase):
    def test_get_current_date_1(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

    def test_get_current_date_2(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

    def test_get_current_date_3(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

    def test_get_current_date_4(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

    def test_get_current_date_5(self):
        timeutils = TimeUtils()
        self.assertEqual(timeutils.get_current_date(), timeutils.datetime.strftime("%Y-%m-%d"))

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: datetime, time
# field_dependencies: self.datetime
# method_dependencies: 


