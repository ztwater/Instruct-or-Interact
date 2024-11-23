class EmailClient:
    def get_occupied_size(self):
        """
        Gets the total size of the emails in the email box.
        :return: The total size of the emails in the email box, float.
        """
        total_size = 0
        for email in self.inbox:
            total_size += email['size']
        return total_size