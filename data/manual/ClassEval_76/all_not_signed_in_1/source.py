class SignInSystem:
    def all_not_signed_in(usernames):
        not_signed_in = []
        for username in usernames:
            if not is_signed_in(username):
                not_signed_in.append(username)
        return not_signed_in