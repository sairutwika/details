import smtplib
import re
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "sairutwika1408@gmail.com"
password = "lkte omxr usrc jmcn"
# Name Validation
while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    text = input("Enter Name: ")
    if pattern.fullmatch(text):
        name = text
        break
    else:
        print("Enter Name in correct format")

while True:
    pattern = re.compile(r'^\d{2}-\d{2}-\d{4}$')
    dob1 = input("Enter Date of Birth (DD-MM-YYYY): ")
    if pattern.fullmatch(dob1):
        dob = dob1
        break
    else:
        print("Enter DOB in correct format")

while True:
    pattern = re.compile(r'^\d{10}$')
    phone1 = input("Enter Mobile Number (10 digits only): ")
    if pattern.fullmatch(phone1):
        phone = phone1
        break
    else:
        print("Enter Mobile in correct format")

insta = input("Enter Instagram ID: ")

while True:
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@gmail\.com$')
    email1 = input("Enter Email (must be Gmail): ")
    if pattern.fullmatch(email1):
        email = email1
        break
    else:
        print("Enter Email in correct format")


email_body = ""


msg = MIMEMultipart()
msg['From'] = username
msg['To'] = email  
msg['Subject'] = "Your Provided Details"
msg.attach(MIMEText(email_body, 'plain'))

# Send Email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
