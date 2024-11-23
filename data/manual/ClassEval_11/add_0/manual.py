### Method Description:
    def add(states, stat):
        """
        Add a status to the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Status to be added,int.
        :return: The status after adding the status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6

        """

### Solution Code:
    def add(states, stat):
        BitStatusUtil.check([states, stat])
        return states | stat

### Source Code:
    def add(current_status, new_status):
        if not isinstance(current_status, str) or not isinstance(new_status, str):
            raise TypeError("Parameters must be of type str")
        
        return current_status + new_status

### Predicted Code:
    def add(self, states: int, stat: int) -> int:
        """
        Add a status to the current status,and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The status after adding the status, int.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Parameters must be of type int")
        
        return states + stat

### Adaptation:
Total number: 17
### Raw Output:
```
    def add(self, states: int, stat: int) -> int:
        """
        Add a status to the current status,and check the parameters whether they are legal.
        :param states: Current status, int.
        :param stat: Status to be added, int.
        :return: The status after adding the status, int.
        """
        if not isinstance(states, int) or not isinstance(stat, int):
            raise TypeError("Parameters must be of type int")
        
        return states + stat
```

### Test Code:
class BitStatusUtilTestAdd(unittest.TestCase):
    def test_add(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 4), 6)

    def test_add_2(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 0), 2)

    def test_add_3(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(0, 0), 0)

    def test_add_4(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(0, 2), 2)

    def test_add_5(self):
        bit_status_util = BitStatusUtil()
        self.assertEqual(bit_status_util.add(2, 2), 2)

### Test Output:
# 5 errors, 0 failures in 5 runs.
# errors:
#     TypeError:
#         test_add: add() missing 1 required positional argument: 'stat'
#         test_add_2: add() missing 1 required positional argument: 'stat'
#         test_add_3: add() missing 1 required positional argument: 'stat'
#         test_add_4: add() missing 1 required positional argument: 'stat'
#         test_add_5: add() missing 1 required positional argument: 'stat'
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: 
# method_dependencies: check


