class EmailClient:
    def fetch(self):
        """
        Retrieves the first unread email in the email box and marks it as read.
        :return: The first unread email in the email box, dict.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        >>> receiver.fetch()
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'}

        """
        import email
        import smtplib

        # Connect to the email server and login
        server = smtplib.SMTP('your_email_server')
        server.login('your_email_address', 'your_password')
    
        # Retrieve the list of unread emails
        server.select('INBOX')
        _, data = server.search(None, 'UNSEEN')
        email_ids = data[0].split()
    
        if email_ids:
            # Get the first unread email
            email_id = email_ids[0]
    
            # Mark the email as read
            server.store(email_id, '+FLAGS', '\\Seen')
    
            # Fetch the email content
            _, email_data = server.fetch(email_id, '(RFC822)')
            raw_email = email_data[0][1]
    
            # Parse the raw email data
            email_message = email.message_from_bytes(raw_email)
    
            # Process the email as needed
            # ...
    
            # Convert email_message to a dictionary
            email_dict = {
                'sender': email_message['From'],
                'receiver': email_message['To'],
                'content': email_message.get_payload(),
                'size': len(str(email_message)),
                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'state': 'read'
            }

            # Add the email_dict to the inbox
            self.inbox.append(email_dict)
            
        # Disconnect from the email server
        server.close()
        server.logout()