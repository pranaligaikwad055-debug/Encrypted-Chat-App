# Encrypted Multi-Client Chat Application

## Project Overview

This project is a secure multi-client chat application developed using Python.  
The application allows multiple users to communicate with each other over a TCP connection while ensuring message security using AES encryption.

Messages are encrypted before transmission and decrypted after receiving, providing secure communication between connected clients.

The project demonstrates concepts of:
- Socket Programming
- Networking
- Cybersecurity
- AES Encryption
- Multi-threading
- Client-Server Architecture

---

# Features

- Secure AES Encryption
- TCP Socket Communication
- Multi-Client Support
- Concurrent Client Handling using Threading
- Message Logging
- Random IV Generation for Security
- Real-Time Messaging

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Main Programming Language |
| Socket Programming | Network Communication |
| AES Encryption | Message Security |
| Threading | Multi-client Support |
| Logging Module | Chat History Logging |

---

# Project Structure

```text
Encrypted-Chat-App/
│
├── chat_app.py
├── README.md
├── requirements.txt
└── chat.log
```

---

# How the Project Works

1. The server starts and waits for clients.
2. Clients connect to the server using TCP sockets.
3. A client types a message.
4. The message is encrypted using AES encryption.
5. Encrypted data is sent to the server.
6. The server broadcasts the encrypted message to other clients.
7. Receiving clients decrypt the message and display it.
8. Messages are logged into a chat log file.

---

# Encryption Used

## AES (Advanced Encryption Standard)

AES is a symmetric encryption algorithm used for secure communication.

### Security Features
- AES Encryption
- Random Initialization Vector (IV)
- Secure Message Transfer
- Encrypted Communication Channel

---

# Installation

## Install Python
Download Python from:

https://www.python.org/downloads/

---

# Install Required Library

Open terminal and run:

```bash
pip install pycryptodome
```

---

# Run the Project

## Start Server

```bash
python chat_app.py server
```

---

## Start Client

Open another terminal and run:

```bash
python chat_app.py client
```

You can open multiple client terminals for group chat.

---

# Example Output

## Server

```text
[SERVER STARTED]
Listening on 127.0.0.1:5555
```

---

## Client 1

```text
You: Hello
```

---

## Client 2

```text
Friend: Hello
```

---

# Logging

All chat messages are saved automatically in:

```text
chat.log
```

---

# Learning Outcomes

Through this project, the following concepts were learned:

- Python Socket Programming
- TCP Communication
- AES Encryption
- Threading in Python
- Client-Server Systems
- Secure Communication
- Networking Basics

---

# Future Improvements

Possible future enhancements:
- GUI using Tkinter or PyQt
- Login Authentication
- End-to-End Encryption
- Database Integration
- File Sharing
- Voice Chat Support

---

# Author

Pranali Gaikwad

---

# License

This project is created for educational and learning purposes.