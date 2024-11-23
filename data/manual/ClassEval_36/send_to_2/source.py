class EmailClient:
    def send_to(email_address, subject, message):
        # Set up the email details
        sender_email = 'your_email@example.com'
        receiver_email = email_address
        email_subject = subject
        email_message = message
    
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