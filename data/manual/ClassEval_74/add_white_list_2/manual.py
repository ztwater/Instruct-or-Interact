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
```
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
```

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


