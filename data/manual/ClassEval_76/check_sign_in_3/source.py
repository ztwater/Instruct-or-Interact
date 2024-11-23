class SignInSystem:
    def check_sign_in(user):
        if user.is_signed_in:
            print("User is signed in.")
        else:
            print("User is not signed in.")