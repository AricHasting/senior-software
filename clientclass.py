#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from collections import deque
import re
import select

# This will be the list of received messages
buffer = deque()
connected = True

def attempt_to_receive():
    """Handles receiving of messages."""
    while connected:
        try:
            ready = select.select([client_socket], [], [])
            if ready[0]:
                msg = client_socket.recv(BUFSIZ).decode("utf8")
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
    """Actually returns a message from buffer if it has one."""
    if buffer:
        return buffer.popleft()
    else:
        return ''

def send(msg):  # event is passed by binders.
    """Handles sending of messages."""
    if(msg == "{quit}"): connected = False
    client_socket.send(bytes(msg, "utf8"))



#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=attempt_to_receive)
receive_thread.start()
