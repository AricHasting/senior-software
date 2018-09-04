#!/usr/bin/env python3
# Credit: https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from collections import deque
import re
import select

# This will be the list of received messages
buffer = deque()
connected = True
client_socket = None


def attempt_to_receive():
    """Handles receiving of messages.
    This method will run and continuously check to see if a message comes in.
    If a message comes in, it'll be added to the buffer."""
    global client_socket
    global connected
    while connected:
        try:
            ready = select.select([client_socket], [], [])
            if ready[0]:
                msg = client_socket.recv(1024).decode("utf8")
                buffer.append(msg)
        except OSError:  # Possibly client has left the chat.
            raise("OSError")
    return

def has_message():
    """Will indicate if a message is ready to be read.""" 
    if buffer:
        return True
    else:
        return False

def receive():
    """Actually returns a message from buffer if it has one.
    If the buffer is empty, an empty string will be returned"""
    if buffer:
        return buffer.popleft()
    else:
        return ''


def send(msg):
    """This will broadcast msg across the chatroom"""
    global connected
    if not connected:
        raise("Can't send message because this client is not connected!")
    """Handles sending of messages."""
    if(msg == "{quit}"): connected = False
    client_socket.send(bytes(msg, "utf8"))

# 
def connect(HOST, PORT):
    """This must be the first client method that is called"""
    ADDR = (HOST, PORT)
    global client_socket
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)

    receive_thread = Thread(target=attempt_to_receive)
    receive_thread.start()
