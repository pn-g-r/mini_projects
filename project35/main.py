import yagmail
import dotenv
import os
 
# Load environment variables from .env file
dotenv.load_dotenv()
password = os.getenv('GMAIL_PASSWORD')
sender_email = 'tt.test.159753159753@gmail.com'
 
# Initialize the yagmail SMTP server
yag = yagmail.SMTP(sender_email, password)
 
# Email content
subject = 'Just wanted to say hi'
body = """
Hi,
 
I just wanted to say hi!
 
Regards
Gigi
"""
 
# Read email addresses from emails.txt
with open('project35/emails.txt', 'r') as file:
    email_addresses = file.readlines()
 
# Remove any surrounding whitespace characters (like newlines)
email_addresses = [email.strip() for email in email_addresses]
 
# Send the email to each address in the list
for recipient_email in email_addresses:
    yag.send(to=recipient_email, 
             subject=subject, 
             contents=body,
             attachments=['project35/emails.txt'])
    print(f'Email sent successfully to {recipient_email}!')