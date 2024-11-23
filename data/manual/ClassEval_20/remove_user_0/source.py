class Chat:
    def remove_user(chat, user):
        if user in chat:
            chat.remove(user)
            print(f"User {user} has been removed from the Chat.")
        else:
            print(f"User {user} is not in the Chat.")
    