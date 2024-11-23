class EmailClient:
    def clear_inbox(self, size):
        """
        Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
        :param size: The size of the email, float.
        """
        while self.get_occupied_size() > size:
            oldest_email = min(self.inbox, key=lambda x: x['size'])
            self.inbox.remove(oldest_email)
