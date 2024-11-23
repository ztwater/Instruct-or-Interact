class Chat:
    def get_messages(user_id):
        # Assuming you have a Chat object with a list of messages
        chat = Chat()
        
        # Create an empty list to store the user's messages
        user_messages = []
        
        # Iterate through all the messages in the chat
        for message in chat.messages:
            # Check if the message is from the specified user
            if message.user_id == user_id:
                # Add the message to the user_messages list
                user_messages.append(message)
        
        # Return the list of user's messages
        return user_messages