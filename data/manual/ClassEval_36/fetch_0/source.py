class EmailClient:
    def fetch():
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
    
        # Disconnect from the email server
        server.close()
        server.logout()