
from tkinter import *
from client import *
from server import *


chat = None
S = None
running = True

def close_window():
    send("{quit}")
    global running
    running = False
    root.destroy()


def listenForMsg():
    while running:
        if has_message():
            display_message(receive())


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


def sendMessage(event):
    if(len(entry.get()) > 0):
        print("This would have sent %s if it was implemented." % entry.get()) # send message here instead of printing
        send(entry.get())
        chat.config(state=NORMAL)
        chat.insert(END, entry.get())
        chat.insert(END, "\n")
        entry.delete(first=0,last="end") # clear the entry
        chat.config(state=DISABLED)
        chat.see(END)


def display_message(msg):
    print("This would have sent %s if it was implemented." % msg) # send message here instead of printing
    chat.config(state=NORMAL)
    chat.insert(END, msg)
    chat.insert(END, "\n")
    entry.delete(first=0,last="end") # clear the entry
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



connect("127.0.0.1", 8080)



receive_msg_thread = Thread(target=listenForMsg)
receive_msg_thread.daemon = True
receive_msg_thread.start()


root.mainloop()


