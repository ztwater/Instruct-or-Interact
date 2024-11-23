class Chat:
    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        """
        user_messages = []
        if username in self.users:
            user_messages = self.users[username]
        return user_messages