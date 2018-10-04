#!/usr/bin/env python3
import client
import time

client.connect("127.0.0.1", 8080)

client.send("Client") # The unique ID will be implemented. This is just so we can quickly test this now

client.send("Hello")
print(client.receive())

client.send("How are you")
print(client.receive())

client.send("That's good")
print(client.receive())