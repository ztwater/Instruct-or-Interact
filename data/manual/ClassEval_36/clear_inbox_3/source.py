class EmailClient:
    def clear_inbox(email_box, size):
        while sum(email_box) > size:
            oldest_email = min(email_box)
            email_box.remove(oldest_email)
        return email_box