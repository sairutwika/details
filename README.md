# details

# 📧 Automated Email Sender with User Input Validation

This Python script collects user details via the command line, validates them, and then sends the details to the user's Gmail account using SMTP.

## 🚀 Features
- Validates user input for **Name, Date of Birth, Mobile Number, and Email**.
- Sends an **automated email** with the collected details.
- Uses **environment variables** for security (no hardcoded credentials).
- Supports **Gmail SMTP** for email sending.

## 📦 Requirements

Before running the script, install the required dependencies:

```sh
pip install python-dotenv
