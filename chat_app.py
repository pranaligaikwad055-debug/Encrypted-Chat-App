import socket
import threading
import logging
import os
import sys

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# ==================================================
# CONFIGURATION
# ==================================================

HOST = "127.0.0.1"
PORT = 5555

# AES key must be exactly 16 bytes
KEY = b"abcdefghijklmnop"

# ==================================================
# ENCRYPTION FUNCTIONS
# ==================================================

def encrypt_message(message):

    iv = os.urandom(16)

    cipher = AES.new(KEY, AES.MODE_CBC, iv)

    encrypted_message = cipher.encrypt(
        pad(message.encode(), AES.block_size)
    )

    return iv + encrypted_message


def decrypt_message(encrypted_message):

    iv = encrypted_message[:16]

    encrypted_data = encrypted_message[16:]

    cipher = AES.new(KEY, AES.MODE_CBC, iv)

    decrypted_message = unpad(
        cipher.decrypt(encrypted_data),
        AES.block_size
    )

    return decrypted_message.decode()


# ==================================================
# SERVER
# ==================================================

clients = []

logging.basicConfig(
    filename="chat.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def broadcast(message, sender):

    for client in clients:

        if client != sender:

            try:
                client.sendall(message)

            except:

                if client in clients:
                    clients.remove(client)


def handle_client(client):

    while True:

        try:

            message = client.recv(4096)

            if not message:
                break

            decrypted = decrypt_message(message)

            print(f"[MESSAGE] {decrypted}")

            logging.info(decrypted)

            broadcast(message, client)

        except Exception as e:

            print("[SERVER ERROR]", e)

            if client in clients:
                clients.remove(client)

            client.close()

            break


def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))

    server.listen()

    print("\n[SERVER STARTED]")
    print(f"Listening on {HOST}:{PORT}\n")

    while True:

        client, address = server.accept()

        print(f"[NEW CONNECTION] {address}")

        clients.append(client)

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


# ==================================================
# CLIENT
# ==================================================

def receive_messages(client):

    while True:

        try:

            message = client.recv(4096)

            if not message:
                break

            decrypted = decrypt_message(message)

            print(f"\nFriend: {decrypted}")

        except Exception as e:

            print("\n[DISCONNECTED]")
            print(e)

            client.close()

            break


def send_messages(client):

    while True:

        try:

            message = input("You: ")

            encrypted = encrypt_message(message)

            client.sendall(encrypted)

        except Exception as e:

            print("[CLIENT ERROR]", e)

            client.close()

            break


def start_client():

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        client.connect((HOST, PORT))

    except:

        print("[UNABLE TO CONNECT TO SERVER]")
        return

    print("\n[CONNECTED TO SERVER]\n")

    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,)
    )

    receive_thread.start()

    send_thread = threading.Thread(
        target=send_messages,
        args=(client,)
    )

    send_thread.start()


# ==================================================
# MAIN
# ==================================================

if len(sys.argv) != 2:

    print("\nUsage:")
    print("Server : python chat_app.py server")
    print("Client : python chat_app.py client")

    sys.exit()

mode = sys.argv[1].lower()

if mode == "server":

    start_server()

elif mode == "client":

    start_client()

else:

    print("Invalid mode")