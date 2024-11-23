class SignInSystem:
    def all_not_signed_in(self):
        not_signed_in = []
        for username in self.users:
            if not self.check_sign_in(username):
                not_signed_in.append(username)
        return not_signed_in