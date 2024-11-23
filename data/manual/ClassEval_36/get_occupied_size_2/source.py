class EmailClient:
    def get_occupied_size(emails):
        total_size = 0
        for email in emails:
            total_size += email.size
        return total_size