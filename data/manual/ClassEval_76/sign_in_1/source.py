class SignInSystem:
    def sign_in(self, username):
        if username in self.users:
            self.users[username] = True
            print(f"User {username} has been signed in.")
        else:
            print(f"User {username} does not exist.")