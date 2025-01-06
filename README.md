# MailSavvy: Email Verification Tool 📧✅

MailSavvy is a Flask-based web application designed to verify email addresses by performing DNS MX record lookups and SMTP communication. The tool provides a user-friendly interface, offering real-time feedback on email validity. Ideal for educational purposes and foundational use cases, MailSavvy serves as a robust starting point for building more advanced email validation workflows.

---

## Features ✨

- **DNS MX Record Lookup** 🌐  
  Checks if the domain of the provided email has valid mail exchange (MX) records.

- **SMTP Communication** 💬  
  Verifies an email address by interacting with the domain's SMTP server.

- **Web-Based Interface** 🖥️  
  A minimalistic and responsive UI for easy email verification.

- **Real-Time Feedback** ⏱️  
  Displays validation results categorized as:
  - **Valid** ✅ : Email address exists and is valid.
  - **Invalid** ❌ : Email address does not exist or is undeliverable.
  - **Error** ⚠️ : Temporary or server-related issues encountered during verification (e.g., no MX records, unreachable server).

- **Lightweight and Easy to Deploy** 🚀  
  Built with Flask, making it simple to set up and use.

---

## Screenshot Previews 📸

### **Valid Email** ✅

The tool successfully verifies the email address:

![Valid Email](/images/valid.png)

### **Invalid Email** ❌
The tool detects an invalid or undeliverable email address:

![Invalid Email](/images/invalid.png)

### **Error** ⚠️
An error occurs during the verification process (e.g., no MX records or server issues):

![Error](/images/error1.png)
![Error](images/error2.png)

---

## **How It Works** 🔄

1. **Input**: Enter an email address in the input field. 📥
2. **MX Record Check**: The tool queries the DNS for MX records of the domain associated with the entered email. 🌐
3. **SMTP Validation**: Establishes a connection to the domain’s SMTP server to verify the existence of the email address. 📧💻
4. **Result**: Displays the outcome as valid, invalid, or error based on the verification process. ✅❌⚠️

---

## Installation Guide 📦

### Prerequisites 🛠️
- Python 3.6 or higher
- Pip (Python Package Manager)

### Steps to Install and Run 🏃‍♂️

1. Clone the Repository:

```bash
git clone https://github.com/iqlipx/MailSavvy.git
cd MailSavvy
```
2. Install Dependencies:

```bash
pip3 install -r requirements.txt
```
3. Run the Application:

```bash
python3 app.py
```
4. Access the Tool:
- Open your browser and visit:

```bash
http://127.0.0.1:5000
```

## Known Issues ⚠️

- **Server Restrictions**: Some mail servers may reject or throttle requests. 🚫
- **False Positives/Negatives**: SMTP responses can vary depending on the server's configuration. ⚖️
- **Timeouts**: DNS queries or SMTP communication may experience delays. ⏳

---

Feel free to modify and use the tool for educational purposes or as a starting point for your projects! 🚀


