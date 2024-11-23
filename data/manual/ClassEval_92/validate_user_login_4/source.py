class UserLoginDB:
    def validate_user_login(username, password):
        # Assuming you have a database with user information
        # You can replace this with your own database query logic
        database = {
            "user1": "password1",
            "user2": "password2",
            "user3": "password3"
        }
    
        if username in database and database[username] == password:
            return True
        else:
            return False