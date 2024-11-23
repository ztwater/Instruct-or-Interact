### Method Description:
    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """

### Solution Code:
    def add_white_list(self, addr):
        if addr in self.white_list:
            return False
        else:
            self.white_list.append(addr)
            return self.white_list

### Source Code:
    def add_white_list(address, whitelist):
        if address not in whitelist:
            whitelist.append(address)

### Predicted Code:
    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """
        if addr not in self.white_list:
            self.white_list.append(addr)
            return self.white_list
        else:
            return False


### Adaptation:
Total number: 14
### Raw Output:
Here is the adapted method `add_white_list` in the class context of `Server`:

```python
class Server:  
    """
    This is a class as a server, which handles a white list, message sending and receiving, and information display.
    """

    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}

    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """
        if addr not in self.white_list:
            self.white_list.append(addr)
            return self.white_list
        else:
            return False

    def del_white_list(self, addr):
        pass

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self, type):
        pass
```

This adapted method adds the `add_white_list` method to the `Server` class. It checks if the given address `addr` is already in the `white_list` of the server instance. If it is not in the list, the address is appended to the `white_list` and the updated `white_list` is returned. If the address already exists in the `white_list`, the method returns `False`.

### Test Code:
class ServerTestAddWhiteList(unittest.TestCase):
    def test_add_white_list_1(self):
        server = Server()
        server.add_white_list(88)
        self.assertEqual(server.white_list, [88])

    def test_add_white_list_2(self):
        server = Server()
        server.add_white_list(88)
        self.assertEqual(server.add_white_list(88), False)

    def test_add_white_list_3(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(11)
        self.assertEqual(server.add_white_list(11), False)

    def test_add_white_list_4(self):
        server = Server()
        server.add_white_list(11)
        self.assertEqual(server.white_list, [11])

    def test_add_white_list_5(self):
        server = Server()
        server.add_white_list(88)
        server.add_white_list(11)
        server.add_white_list(22)
        self.assertEqual(server.add_white_list(22), False)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.white_list
# method_dependencies: 


