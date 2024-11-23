class Chat:
    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        else:
            return False