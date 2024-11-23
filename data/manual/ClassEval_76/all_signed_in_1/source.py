class SignInSystem:
    def all_signed_in(users):
        for user in users:
            if not user.is_signed_in():
                return False
        return True