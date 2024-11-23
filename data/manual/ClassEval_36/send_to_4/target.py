class EmailClient:
    def send_to(self, recv, content, size):
        """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        """
        # Set up the email details
        sender_email = self.addr
        receiver_email = recv
        email_subject = "New Email"
        email_message = content

        # Create the email
        email = MIMEText(email_message)
        email['Subject'] = email_subject
        email['From'] = sender_email
        email['To'] = receiver_email

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, 'your_password')
            smtp.send_message(email)
            self.save_to_inbox(recv, content, size)
            return True
