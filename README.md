# Simple Email Web Application Using SMTP

This project is a lightweight and efficient email web application designed to send emails via SMTP without relying on external libraries. It utilizes Python and Flask for backend functionality and offers a user-friendly interface for seamless interaction.

---

## Features

### 1. **Raw SMTP Implementation**
- Directly establishes a connection with an SMTP server using raw sockets for lightweight, library-free email handling.

### 2. **TLS Encryption**
- Ensures secure communication by implementing STARTTLS to encrypt SMTP connections.

### 3. **User Authentication**
- Uses Base64-encoded credentials for authentication via the `AUTH LOGIN` mechanism.

### 4. **Email Transmission**
- Sends email messages by specifying sender, recipient, and message content, adhering to SMTP protocols.

---

## System Architecture

### 2.1 Client (Frontend)
#### Functionality:
- Provides a web interface for the user to input email details (sender’s email, recipient’s email, subject, message).
- Uses HTML, CSS, and JavaScript to design and build the frontend interface.
- JavaScript (Fetch API) is used to send data to the backend.

#### Interaction:
- The frontend sends a POST request to the backend server with the email details when the user submits the form. The backend processes the request and responds with a success or failure message.

### 2.2 Server (Backend)
#### Functionality:
- Processes the incoming email data from the client.
- Validates the email fields and checks for correct formats (e.g., valid email addresses).
- Sends the email via an SMTP server using the SMTP protocol.
- Manages CORS: The server handles Cross-Origin Resource Sharing to allow secure communication between the frontend and backend.

#### Technology:
- Built using Python (Flask), a lightweight web framework.
- Flask-CORS is used to manage cross-origin requests securely.

#### Interaction:
- The backend receives HTTP POST requests from the frontend.
- It processes the email data, interacts with the SMTP Layer to send the email, and responds with a success or error message.

### 2.3 SMTP Layer
#### Functionality:
- Handles the communication between the server and the SMTP server (e.g., Gmail’s SMTP server).
- Ensures secure transmission of email data using TLS encryption.
- Uses the SMTP protocol for email sending, handling commands like EHLO, AUTH LOGIN, MAIL FROM, RCPT TO, DATA, and QUIT.

#### Technology:
- Implemented with Python libraries such as socket, ssl, and base64 for secure communication and SMTP command handling.

#### Interaction:
- The backend uses this layer to send the email to the recipient by communicating with an SMTP server.

---

## File Structure

### Frontend:
- **`index.html`**: The main user interface, allowing users to input email details.
- **`emailSender.js`**: A JavaScript file handling the communication between the frontend and backend.

### Backend:
- **`email_handler.py`**: The core Flask-based script that manages SMTP processes, including connection establishment, encryption, authentication, and email transmission.

---

## How It Works

1. **User Interaction**
   - The user fills out an email form on `index.html`.

2. **Frontend-Backend Communication**
   - Form data is sent to the backend via AJAX requests managed by `emailSender.js`.

3. **Backend SMTP Processing**
   - The Flask application (`email_handler.py`) executes the following steps:
     - Establishes a connection to the SMTP server.
     - Secures the connection using STARTTLS.
     - Authenticates the user via Base64-encoded credentials.
     - Transmits the email.

4. **Feedback to the User**
   - The backend sends a success or error response, which is displayed to the user on the frontend.

---

## Prerequisites

### 1. **Software Requirements**
- **Python**: Version 3.6 or newer is required.
- **Flask**: Install Flask via `pip install flask`.
- **Flask-CORS**: Install via `pip install flask-cors`.

### 2. **SMTP Server Access**
- An SMTP server is necessary (e.g., Gmail, Yahoo).
- Credentials:
  - Email address
  - App password (if using Gmail, generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en)).

---

## Installation and Setup

### 1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-email-webapp.git
   cd simple-email-webapp
   ```

### 2. Install dependencies:
   ```bash
   pip install flask flask-cors
   ```

### 3. Run the Flask application:
   ```bash
   python email_handler.py
   ```

### 4. Open the application in your web browser:
   - Navigate to `http://127.0.0.1:5000`.

---

## Usage

1. Open the application in your browser.
2. Enter the required details in the email form:
   - Sender email address
   - App password
   - Recipient email address
   - Subject
   - Message content
3. Click "Send".
4. View success or error messages displayed on the UI.

---

## Example SMTP Server Configuration

### Gmail SMTP:
- **Server Address**: `smtp.gmail.com`
- **Port**: 587
- **Requirements**:
  - Enable "Less Secure App Access" or generate an app password.

### Other Servers:
- Check the provider’s SMTP documentation for details.

---

## Troubleshooting

### 1. Flask Server Not Running
- **Issue**: The Flask server isn’t running.
- **Solution**: Run the following command:
  ```bash
  python email_handler.py
  ```
  Ensure Flask is installed and that the correct Python interpreter is selected.

### 2. "Connection Refused" Error
- **Issue**: The client cannot connect to the Flask server.
- **Solution**:
  - Ensure the Flask server is running at `http://127.0.0.1:5000`.
  - Check for firewalls or antivirus blocking the connection.

### 3. "Failed to Send Email" Error
- **Issue**: Authentication failed or email format is invalid.
- **Solution**:
  - Verify sender email and app password.
  - Ensure valid email formats for sender and recipient.

### 4. "Timeout" Error
- **Issue**: The request takes too long.
- **Solution**:
  - Check network connection.
  - Adjust timeout settings or change SMTP ports if needed.

---

## Security Note

To prevent sensitive data exposure:
- Never hardcode credentials in the code.
- Use environment variables to store sensitive information.
- Avoid sharing app passwords in public repositories.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and submit a pull request.

---

## Acknowledgments

- Python and Flask for making backend development seamless.
- SMTP protocol documentation for guidance.
- Frontend libraries and tools for simplifying UI development.
