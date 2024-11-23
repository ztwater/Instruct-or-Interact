class SignInSystem:
    def all_not_signed_in(self):
        not_signed_in = []
        for username, is_signed_in in self.users.items():
            if not is_signed_in:
                not_signed_in.append(username)
        return not_signed_in