class EmailClient:
    def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}

        """
        sender_email = self.addr
        receiver_email = recv.addr
        email_subject = content
        email_message = size

        email = MIMEText(email_message)
        email['Subject'] = email_subject
        email['From'] = sender_email
        email['To'] = receiver_email

        if recv.is_full_with_one_more_email(size):
            return False

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, 'your_password')
            smtp.send_message(email)

        email_data = {
            'sender': sender_email,
            'receiver': receiver_email,
            'content': email_subject,
            'size': size,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'state': 'unread'
        }

        recv.inbox.append(email_data)
        return True