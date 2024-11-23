class SignInSystem:
    def check_sign_in(self, username):
        """
        Check if a user is signed in.
        :param username: str, the username to be checked.
        :return: bool, True if the user is signed in, False if the user does not exist or is not signed in.
        """
        if username in self.users:
            if self.users[username].is_signed_in:
                return True
            else:
                return False
        else:
            return False