class SignInSystem:
    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"User {user} added successfully.")
        else:
            print(f"User {user} already exists in the system.")