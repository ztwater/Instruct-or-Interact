class EmailClient:
    def is_full_with_one_more_email(self, size):
        """
        Determines whether the email box is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the email box is full, False otherwise.
        """
        total_size = self.get_occupied_size() + size
        if total_size <= self.capacity:
            return False
        else:
            return True