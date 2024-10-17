import psutil
import yagmail
import dotenv
import os
from datetime import datetime
 
# Load environment variables
dotenv.load_dotenv()
password = os.getenv('GMAIL_PASSWORD')
sender_email = 'tt.test.159753159753@gmail.com'  # It's better to store this in .env
 
# Create a yagmail.SMTP object
yag = yagmail.SMTP(sender_email, password)
 
# Collect system metrics using psutil
cpu_usage = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')
 
# Format the metrics into a readable message body
body = f"""
Hi,
 
Here are the current system metrics:
 
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
CPU Usage: {cpu_usage}%
Memory Total: {memory_info.total / (1024 * 1024):.2f} MB
Memory Used: {memory_info.used / (1024 * 1024):.2f} MB ({memory_info.percent}%)
Disk Total: {disk_usage.total / (1024 * 1024 * 1024):.2f} GB
Disk Used: {disk_usage.used / (1024 * 1024 * 1024):.2f} GB ({disk_usage.percent}%)
 
Regards,
Your Python Script
"""
 
# Send the email
yag.send(
    to='tt.test.159753159753@gmail.com',
    subject='Daily System Metrics',
    contents=body
)
 
print('Email sent successfully!')