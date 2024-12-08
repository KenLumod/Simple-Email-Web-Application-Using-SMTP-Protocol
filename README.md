Simple Email Web App Using SMTP
This project is a simple email web application that allows users to send emails using SMTP without relying on external libraries. It leverages Python and Flask for seamless interaction between the frontend and backend.

Features
SMTP Implementation: Establishes a connection to an SMTP server using raw sockets.
TLS Encryption: Secures communication with STARTTLS.
User Authentication: Authenticates with the server using Base64-encoded credentials via AUTH LOGIN.
Email Transmission: Sends email by specifying the sender, recipient, and message content.

File Structure
index.html: The main UI of the application
emailSender.js: JavaScript file for managing frontend-backend communication.
email_handler.py: Flask-based backend script that executes the SMTP logic for sending emails.
How It Works
The user fills out the form on the index.html page.
The form data is sent to the backend using the custom JavaScript file, emailSender.js.
The Flask backend (email_handler.py) processes the data and handles the SMTP process:
Establishing a connection to the SMTP server.
Securing the connection with TLS.
Authenticating the user.
Sending the email.
A success or error message is returned to the frontend and displayed to the user.

Prerequisites
Python 3.6+: Required for running email_handler.py.
Flask: Ensure Flask is installed (pip install flask).
SMTP Server Access: You need an SMTP server (e.g., Gmail) and credentials (email and app password).
