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
            print(msg)
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
    chat = Text(chatFrame, bg="#E8E8E8")
    chat.config(state=DISABLED)

    chat.pack()


    scroll = Scrollbar(chatFrame)
    chat.pack(side=LEFT, fill=Y)
    scroll.pack(side=LEFT, fill=Y)
    scroll.config(command=chat.yview)
    chat.config(yscrollcommand=scroll.set)

    send = Button(sendFrame,text="Send", command=sendMessage)

    send.pack(side=BOTTOM)

    scroll2 = Scrollbar(sendFrame, command=entry.yview)
    chat.pack(side=LEFT, fill=Y)
    scroll2.pack( side=RIGHT, fill=Y)
    scroll2.config(command=entry.yview)
    entry.config(yscrollcommand=scroll2.set)
    entry.pack(side = BOTTOM)

    ttsLabel = Label(chatFrame, text="Text to Speech")
    ttsLabel.pack()
    ttsToggle.pack()


def sendMessage(event = None):
    global name
    global Im_a_wizard_harry
    if(len(entry.get(1.0,END)) > 0):
        # check for wizard command
        if parser.getCommand(entry.get(1.0,END).lower()) == "wizard":
            sendHagrid()
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
            elif parser.getCommand(entry.get(1.0,END).lower()) == "model"\
                    and Im_a_wizard_harry:
                # update local avatar model
                # then send message unaltered
                msg = entry.get(1.0,END)
                avatar_model = parser.getArgument(msg)[0]
                avatar_model_var.set(avatar_model)
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


def text_to_speech(msg):
    # only use text to speech for messages from other user and if text to speech is turned on
    if msg.startswith(name.rstrip()) and (ttsToggle["text"] == "On"):
        msg.rstrip()
        msg = msg[len(name):len(msg)]
        tts = gTTS(text=msg, lang='en', slow=False)
        tts.save("tts.mp3")
        os.system("mpg123 tts.mp3")


def display_message(msg):
    chat.config(state=NORMAL)
    chat.insert(END, msg)
    chat.insert(END, "\n")
    chat.config(state=DISABLED)
    chat.see(END)

    tts_thread = Thread(target=text_to_speech, args=(msg,))
    tts_thread.daemon = True
    tts_thread.start()


def ttsButton():
    if ttsToggle["text"] == "On":
        ttsToggle["text"] = "Off"
    else:
        ttsToggle["text"] = "On"

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
    entry = Text(sendFrame, cursor="xterm", bd=5, bg="#E8E8E8")

    # text to speech is on by default
    ttsToggle = Button(chatFrame, text="On", command=ttsButton)

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


