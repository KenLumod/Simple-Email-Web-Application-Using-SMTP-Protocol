import socket
import ssl
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(email, app_password, receiver_email, subject, message):
    email_content = f"Subject: {subject}\n\n{message}"

    try:
        # Establish a connection to the SMTP server
        client_socket = socket.create_connection((SMTP_SERVER, SMTP_PORT))
        client_socket.recv(1024).decode()

        # Say EHLO to the server
        client_socket.send(b"EHLO client\r\n")
        client_socket.recv(1024).decode()

        # Start TLS encryption
        client_socket.send(b"STARTTLS\r\n")
        client_socket.recv(1024).decode()

        # Wrap the socket with SSL/TLS
        context = ssl.create_default_context()
        secure_socket = context.wrap_socket(client_socket, server_hostname=SMTP_SERVER)

        # Say EHLO again after TLS handshake
        secure_socket.send(b"EHLO client\r\n")
        secure_socket.recv(1024).decode()

        # Authenticate with the server using AUTH LOGIN
        secure_socket.send(b"AUTH LOGIN\r\n")
        secure_socket.recv(1024).decode()

        # Send the email and password (Base64 encoded)
        secure_socket.send(base64.b64encode(email.encode()) + b"\r\n")
        response = secure_socket.recv(1024).decode()
        if "535" in response:
            raise Exception("Authentication failed: Check email or app password.")

        secure_socket.send(base64.b64encode(app_password.encode()) + b"\r\n")
        response = secure_socket.recv(1024).decode()
        if "535" in response:
            raise Exception("Authentication failed: Check your app password.")

        # Specify sender and recipient
        secure_socket.send(f"MAIL FROM:<{email}>\r\n".encode())
        response = secure_socket.recv(1024).decode()
        if "550" in response:
            raise Exception("Invalid sender email address.")

        secure_socket.send(f"RCPT TO:<{receiver_email}>\r\n".encode())
        response = secure_socket.recv(1024).decode()
        if "550" in response:
            raise Exception("Invalid recipient email address.")

        # Send the email data
        secure_socket.send(b"DATA\r\n")
        response = secure_socket.recv(1024).decode()
        if "554" in response:
            raise Exception("Message rejected. Check the content of your email.")

        secure_socket.send((email_content + "\r\n.\r\n").encode())
        response = secure_socket.recv(1024).decode()
        if "554" in response:
            raise Exception("Message rejected. Check the content of your email.")

        # Quit the SMTP session
        secure_socket.send(b"QUIT\r\n")
        secure_socket.recv(1024).decode()

        secure_socket.close()
        return True, "Email sent successfully!"

    except Exception as e:
        print(f"Error: {e}")  # Print to the terminal
        return False, str(e)

@app.route('/send-email', methods=['POST'])
def handle_email():
    data = request.json
    email = data.get("email")
    app_password = data.get("app_password")
    receiver_email = data.get("receiver_email")
    subject = data.get("subject")
    message = data.get("message")

    if not all([email, app_password, receiver_email, subject, message]):
        return jsonify({"success": False, "message": "All fields are required."}), 400

    # Validate the format of the sender and receiver email addresses
    if "@" not in email or "@" not in receiver_email:
        return jsonify({"success": False, "message": "Invalid email address format."}), 400

    success, msg = send_email(email, app_password, receiver_email, subject, message)

    if success:
        return jsonify({"success": True, "message": msg}), 200
    else:
        return jsonify({"success": False, "message": msg}), 400

if __name__ == '__main__':
    app.run(debug=True)
