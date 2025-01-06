from flask import Flask, render_template, request, jsonify
import dns.resolver
import smtplib
import socket

app = Flask(__name__)


def find_mx(domain):
    """Find the MX records for a domain using DNS lookup"""
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        mx_record = str(answers[0].exchange)
        return mx_record
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN) as e:
        return None

def verify_email_smtp(email):
    """Verify email via SMTP by contacting the mail server"""
    try:
        domain = email.split('@')[1]
        mx = find_mx(domain)
        if not mx:
            return "No MX records found for domain", False

        # Connect to the SMTP server
        with smtplib.SMTP(mx, 25, timeout=10) as server:
            server.set_debuglevel(0)

            # Say hello to the server
            server.helo()

            # Send MAIL FROM command
            server.mail("root@localhost")

            # Send RCPT TO command for the provided email address
            code, message = server.rcpt(email)
            
            # Check the response code
            if code == 250:
                return "Email is valid", True
            elif code == 550:
                return "Email is invalid", False
            else:
                return "Unknown status, temporary delivery failure", None
    except (smtplib.SMTPException, socket.error) as e:
        
        return "Error verifying email. Please try again later.", False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    email = request.form['email']
    if not email:
        return jsonify({'status': 'error', 'message': 'Email address is required'})

    # Validate the email format
    if '@' not in email or '.' not in email.split('@')[1]:
        return jsonify({'status': 'error', 'message': 'Invalid email format'})

    status_message, verified = verify_email_smtp(email)

    if verified is None:
        return jsonify({'status': 'error', 'message': status_message})
    elif not verified:
        return jsonify({'status': 'invalid', 'message': status_message})
    else:
        return jsonify({'status': 'success', 'message': status_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
