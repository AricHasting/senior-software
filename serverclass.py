#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


accepting = True
SERVER = socket(AF_INET, SOCK_STREAM)
clients = {}
addresses = {}


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while accepting:
        client, client_address = SERVER.accept()
        # print("%s:%s has connected." % client_address)
        # client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
    return


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(BUFSIZ).decode("utf8")
    # welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    # client.send(bytes(welcome, "utf8"))
    # msg = "%s has joined the chat!" % name
    # broadcast(bytes(msg, "utf8"))
    if name in clients.values():
        raise 'This name is already being used!'
    elif name == '':
        raise 'This name is empty!'
    
    clients[client] = name

    while accepting:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            # broadcast(bytes("%s has left the chat." % name, "utf8"))
            break
    return


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    # print ('Broadcasting ', msg)
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)



def startserver(HOST, PORT):
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    SERVER.bind(ADDR)
    SERVER.listen(5)
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()

def closeserver():
    accepting = False
    SERVER.close()
