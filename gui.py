from tkinter import *
from client import *
from server import *
import time
import datetime


chat = None
S = None
running = True
name = None
fileName = None

def close_window():
    send("{quit}")
    global running
    running = False
    root.destroy()


def listenForMsg():
    while running:
        if has_message():
            msg = receive()
            print (msg)
            display_message(msg)
            log = "Message Received-" + msg
            appendToLog(log)
        else:
            time.sleep(1)


def defineFile(name):
    global fileName
    fileName = name

def appendToLog(msg):
    global fileName
    with open(fileName, 'a') as f:
        f.write(msg)


def createAvatar():
    # replace this with an avatar widget
    avatar = Label(avatarFrame,text = "avatar") # replace this with the image of the avatar
    avatar.pack()

def createChat():
    global chat
    # replace this with a chat widget
    chatString = "chat"
    chat = Text(chatFrame)
    chat.config(state=DISABLED)

    chat.pack()


    scroll = Scrollbar(chatFrame)
    chat.pack(side=LEFT, fill=Y)
    scroll.pack(side=LEFT, fill=Y)
    scroll.config(command=chat.yview)
    chat.config(yscrollcommand=scroll.set)

    send = Button(sendFrame,text="send", command=sendMessage)
    send.pack(side=BOTTOM)
    entry.pack(side = BOTTOM)



def sendMessage(event = None):
    global name
    if(len(entry.get()) > 0):
        if (name == None):
            name = entry.get()
            send(name)
            entry.delete(first=0,last="end")
        else:
            msg = name + ':'
            msg = msg + entry.get()
            send(msg)
            chat.config(state=NORMAL)
            display_message(msg)
            entry.delete(first=0,last="end")


def display_message(msg):
    chat.config(state=NORMAL)
    chat.insert(END, msg)
    chat.insert(END, "\n")
    chat.config(state=DISABLED)
    chat.see(END)


root = Tk()
root.title("Paired Programming")

# can change the size if necessary
windowWidth = 800
windowHeight = 800

size = str(windowWidth) + "x" + str(windowHeight)
root.geometry(size)

# the colors are just there to differentiate the frames, should change later
avatarFrame = Frame(root, bg = "red",width=windowWidth, height=windowHeight/3, bd=5)
chatFrame = Frame(root, bg="blue", width=windowWidth, height=windowHeight/3, bd=5)
sendFrame = Frame(root, bg="white", width=windowWidth, height=windowHeight/6, bd=5)
avatarFrame.pack(fill=BOTH, expand=1)
chatFrame.pack(fill=BOTH,expand=1)
sendFrame.pack(fill=BOTH, expand=1)
entry = Entry(chatFrame,bd=5)


createAvatar()
createChat()

root.bind('<Return>', sendMessage)
root.protocol("WM_DELETE_WINDOW", close_window)


now = datetime.datetime.now()

defineFile("VideoLog_" + datetime.datetime.now().strftime("%m") +
 "_" + datetime.datetime.now().strftime("%d") +
 "_" + datetime.datetime.now().strftime("%y"))

# connect("129.244.98.101", 8080)
connect("127.0.0.1", 8080)



receive_msg_thread = Thread(target=listenForMsg)
receive_msg_thread.daemon = True
receive_msg_thread.start()


root.mainloop()


