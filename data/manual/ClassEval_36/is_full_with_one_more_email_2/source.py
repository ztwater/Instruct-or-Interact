class EmailClient:
    def is_full_with_one_more_email(email_box_size, email_size):
        total_size = sum(email_box_size)
        if total_size + email_size <= 100:
            return False
        else:
            return True