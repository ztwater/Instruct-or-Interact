class Chat:
    def get_messages(self, username):
        """
        Get all the messages of a user from the Chat.
        :param username: The user's name, str.
        :return: A list of messages, each message is a dictionary with keys 'sender', 'receiver', 'message', 'timestamp'.
        """
        user_messages = []
        
        if username in self.users:
            # Get the list of messages for the specified user
            messages = self.users[username]
            
            # Iterate through all the messages
            for message in messages:
                # Add the message to the user_messages list
                user_messages.append({
                    'sender': message['sender'],
                    'receiver': message['receiver'],
                    'message': message['message'],
                    'timestamp': message['timestamp']
                })
        
        # Return the list of user's messages
        return user_messages