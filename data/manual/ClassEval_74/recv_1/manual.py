### Method Description:
    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the infomation; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """

### Solution Code:
    def recv(self, info):
        if not isinstance(info, dict) or "addr" not in info or "content" not in info:
            return -1
        addr = info["addr"]
        content = info["content"]
        if addr not in self.white_list:
            return False
        else:
            self.receive_struct = {"addr": addr, "content": content}
            return self.receive_struct["content"]

### Source Code:
    def recv(address, content, whitelist):
        if address in whitelist:
            return content
        else:
            return None

### Predicted Code:
    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the information; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """
        if info["addr"] in self.white_list:
            return info["content"]
        else:
            return False

### Adaptation:
Total number: 15
### Raw Output:
```python
def recv(self, info):
    """
    Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
    :param info: dict, information dictionary containing address and content
    :return: if successfully received, return the content of the information; otherwise, return False
    >>> server.recv({"addr":88,"content":"abc"})
    abc
    """
    if info["addr"] in self.white_list:
        return info["content"]
    else:
        return False
```

### Test Code:
class ServerTestRecv(unittest.TestCase):
    def test_recv_1(self):
        server = Server()
        server.add_white_list(88)
        server.recv({"addr": 88, "content": "abc"})
        self.assertEqual(server.receive_struct, {"addr": 88, "content": "abc"})

    def test_recv_2(self):
        server = Server()
        server.add_white_list(88)
        flag = server.recv({"addr": 66, "content": "abc"})
        self.assertEqual(server.receive_struct, {})
        self.assertEqual(flag, False)

    def test_recv_3(self):
        server = Server()
        flag = server.recv([88])
        self.assertEqual(server.receive_struct, {})
        self.assertEqual(flag, -1)

    def test_recv_4(self):
        server = Server()
        flag = server.recv({"addr": 88})
        self.assertEqual(server.receive_struct, {})
        self.assertEqual(flag, -1)

    def test_recv_5(self):
        server = Server()
        flag = server.recv({"content": "abc"})
        self.assertEqual(server.receive_struct, {})
        self.assertEqual(flag, -1)

### Test Output:
# 2 errors, 2 failures in 5 runs.
# errors:
#     KeyError:
#         test_recv_5: 'addr'
#     TypeError:
#         test_recv_3: list indices must be integers or slices, not str
# failures:
#     AssertionError:
#         test_recv_1: {} != {'addr': 88, 'content': 'abc'}
#         test_recv_4: False != -1


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.receive_struct, self.white_list
# method_dependencies: 


