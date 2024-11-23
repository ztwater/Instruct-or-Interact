### Method Description:
    def all_not_signed_in(self):
        """
        Get a list of usernames that are not signed in.
        :return: list[str], a list of usernames that are not signed in.
        >>> signInSystem = SignInSystem()
        >>> signInSystem.add_user("a")
        True
        >>> signInSystem.add_user("b")
        True
        >>> signInSystem.all_not_signed_in()
        ['a', 'b']
        """

### Solution Code:
    def all_not_signed_in(self):
        not_signed_in_users = []
        for username, signed_in in self.users.items():
            if not signed_in:
                not_signed_in_users.append(username)
        return not_signed_in_users

### Source Code:
    def all_not_signed_in(usernames):
        not_signed_in = []
        for username in usernames:
            if not is_signed_in(username):
                not_signed_in.append(username)
        return not_signed_in

### Predicted Code:
    def all_not_signed_in(self):
        not_signed_in = []
        for username, is_signed_in in self.users.items():
            if not is_signed_in:
                not_signed_in.append(username)
        return not_signed_in

### Adaptation:
Total number: 12
### Raw Output:
```python
def all_not_signed_in(self):
    not_signed_in = []
    for username, is_signed_in in self.users.items():
        if not is_signed_in:
            not_signed_in.append(username)
    return not_signed_in
```

### Test Code:
class SignInSystemTestAllNotSignedIn(unittest.TestCase):
    def test_all_not_signed_in_1(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.sign_in("user1")
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)

    def test_all_not_signed_in_2(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.add_user("user2")
        result = signin_system.all_not_signed_in()
        self.assertEqual(["user1", "user2"], result)

    def test_all_not_signed_in_3(self):
        signin_system = SignInSystem()
        signin_system.add_user("aaa")
        signin_system.sign_in("aaa")
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)

    def test_all_not_signed_in_4(self):
        signin_system = SignInSystem()
        signin_system.add_user("user1")
        signin_system.add_user("aaa")
        signin_system.sign_in("user1")
        result = signin_system.all_not_signed_in()
        self.assertEqual(['aaa'], result)

    def test_all_not_signed_in_5(self):
        signin_system = SignInSystem()
        result = signin_system.all_not_signed_in()
        self.assertEqual([], result)

### Test Output:
# 0 errors, 0 failures in 5 runs.
# errors:
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.users
# method_dependencies: 


