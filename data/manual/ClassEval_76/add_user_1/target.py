class SignInSystem:
    def add_user(self, username):
        """
        Add a user to the sign-in system if the user wasn't in the self.users.
        And the initial state is False.
        :param username: str, the username to be added.
        :return: bool, True if the user is added successfully, False if the user already exists.
        """
        if username not in self.users:
            self.users[username] = False
            print(f"User {username} added successfully.")
            return True
        else:
            print(f"User {username} already exists in the system.")
            return False