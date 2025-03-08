import smtplib

def send_email(sender_email, password, recipient_email, subject, body, smtp_server):
    """
    Parameters:
    -----------
    sender_email : str
        Email address of the sender
    password : str
        Password or app password for the sender's email account
    recipient_email : str
        Email address of the recipient
    subject : str
        Subject of the email
    body : str
        Body content of the email
    smtp_server : str
        SMTP server address (e.g., 'smtp.gmail.com')
    """
    # Construct the email message
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        # Connect to the server
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()  # Upgrade to secure connection
        
        # Login to the email account
        server.login(sender_email, password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        return True
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False