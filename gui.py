from avatar import Avatar_widget
from gtts import gTTS
from tkinter import *
from client import *
from server import *
import time
import datetime
import parser
import os

chat = None
S = None
running = True
name = None
fileName = None
avatar_state_var = None
Im_a_wizard_harry = False

def close_window():
    send("{quit}")
    global running
    running = False
    root.destroy()


def listenForMsg():
    global avatar_state_var
    while running:
        if has_message():
            msg = receive()
            # If current user is Dorothy,
            # parse message for avatar commands
            avatar_state = False
            if not Im_a_wizard_harry:
                avatar_state = parser.getAvatar(msg)
            if avatar_state != False:
                avatar_state_var.set(avatar_state)
            else:
                print (msg)
                display_message(msg)
            log = "Message Received-" + str(msg)
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
    avatar = Avatar_widget(avatarFrame, windowWidth/2, windowHeight/3)
    global avatar_state_var 
    avatar_state_var = avatar.get_state_var()

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

    entry.config(yscrollcommand=scroll.set)
    entry.pack(side = BOTTOM)




def sendMessage(event = None):
    global name
    global Im_a_wizard_harry
    if(len(entry.get(1.0,END)) > 0):
        # check for wizard command
        if parser.getCommand(entry.get(1.0,END).lower()) == "wizard":
            Im_a_wizard_harry = True
            entry.delete(1.0,END)
        else:
            # check for avatar command
            if parser.getCommand(entry.get(1.0,END).lower()) == "avatar"\
                    and Im_a_wizard_harry:
                # update local avatar state
                # then send message unaltered
                msg = entry.get(1.0,END)
                avatar_state = parser.getAvatar(msg)
                avatar_state_var.set(avatar_state)
                send(msg)
                entry.delete(1.0,END)
            elif (name == None):
                name = entry.get(1.0,END)
                name.rstrip()
                send(name)
                entry.delete(1.0,END)
            else:
                msg = name.rstrip() + ": "
                #text = entry.get(1.0,END)
                #print(text)
                msg = msg + entry.get(1.0,END)
                send(msg)
                chat.config(state=NORMAL)
                display_message(msg)
                entry.delete(1.0,END)


def display_message(msg):
    chat.config(state=NORMAL)
    chat.insert(END, msg)
    chat.insert(END, "\n")
    chat.config(state=DISABLED)
    if msg.startswith(name.rstrip()): # change this to not
        msg.rstrip()
        msg = msg[len(name):len(msg)]
        tts = gTTS(text=msg, lang='en', slow=False)
        tts.save("tts.mp3")
        os.system("mpg123 tts.mp3")
    chat.see(END)

if __name__=="__main__":
    root = Tk()
    root.title("Wizard of Oz")

    # can change the size if necessary
    windowWidth = 800
    windowHeight = 800

    size = str(windowWidth) + "x" + str(windowHeight)
    root.geometry(size)

    # the colors are just there to differentiate the frames, should change later
    avatarFrame = Frame(root, bg = "white",width=windowWidth, height=windowHeight/3, bd=5)
    chatFrame = Frame(root, bg="white", width=windowWidth, height=windowHeight/3, bd=5)
    sendFrame = Frame(root, bg="white", width=windowWidth, height=windowHeight/6, bd=5)
    avatarFrame.pack(fill=BOTH, expand=1)
    chatFrame.pack(fill=BOTH,expand=1)
    sendFrame.pack(fill=BOTH, expand=1)
    #entry = Entry(chatFrame,bd=5)
    entry = Text(sendFrame, cursor="xterm", height=5, bd=5, bg="#E8E8E8")


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


