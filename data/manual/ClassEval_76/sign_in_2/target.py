class SignInSystem:
    def sign_in(self, username):
        if username in self.users:
            self.users[username] = True
            return True
        else:
            return False