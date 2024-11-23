class SignInSystem:
    def sign_in(self, username):
        """
        Sign in a user if the user was in the self.users and change the state to True.
        :param username: str, the username to be signed in.
        :return: bool, True if the user is signed in successfully, False if the user does not exist.
        """
        if username in self.users:
            self.users[username] = True
            print(f"User {username} has been signed in.")
            return True
        else:
            print(f"User {username} does not exist.")
            return False