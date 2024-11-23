class SignInSystem:
    def all_signed_in(self):
        """
        Check if all users are signed in.
        :return: bool, True if all users are signed in, False otherwise.
        """
        for user in self.users.values():
            if not user.is_signed_in():
                return False
        return True