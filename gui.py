from avatar import Avatar_widget
from tkinter import *
from client import *
from server import *
import time
import datetime
import parser

chat = None
S = None
running = True
name = None
fileName = None
avatar_w = None
avatar_model_var = None
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
                if parser.getCommand(msg.lower()) == "avatar":
                    avatar_state = parser.getAvatar(msg)
                elif parser.getCommand(msg.lower()) == "model":
                    avatar_state = parser.getArguments(msg)[0]
            if avatar_state != False:
                avatar_state_var.set(avatar_state)
            if avatar_model != False:
                avatar_model_var.set(avatar_model)
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
    global avatar_w
    global avatar_model_var
    global avatar_state_var 
    avatar_w = Avatar_widget(avatarFrame, windowWidth/2, windowHeight/3)
    avatar_model_var, avatar_state_var = avatar_w.get_state_var()

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

# set Im_a_wizard_harry to true
# Add wizard controls to GUI
def sendHagrid():
    global avatar_w
    global Im_a_wizard_harry
    Im_a_wizard_harry = True
    avatar_w.reveal_controls()

def sendMessage(event = None):
    global name
    if(len(entry.get()) > 0):
        # check for wizard command
        msg = entry.get()
        if parser.getCommand(msg.lower()) == "wizard":
            sendHagrid() # Im_a_wizard_harry = true
        else:
            # check for avatar state command
            if parser.getCommand(msg.lower()) == "avatar"\
                    and Im_a_wizard_harry:
                # update local avatar state
                # then send message unaltered
                avatar_state = parser.getAvatar(msg)
                avatar_state_var.set(avatar_state)
                send(msg)
            # check for avatar model command
            elif parser.getCommand(msg.lower()) == "model"\
                    and Im_a_wizard_harry:
                # update local avatar model
                # then send message unaltered
                avatar_model = parser.getArguments(msg)[0]
                avatar_model_var.set(avatar_model)
                send(msg)
            elif (name == None):
                name = msg
                send(name)
            else:
                msg = name + ':' + msg
                send(msg)
                chat.config(state=NORMAL)
                display_message(msg)
        # clear entry field
        entry.delete(first=0,last="end")


def display_message(msg):
    chat.config(state=NORMAL)
    chat.insert(END, msg)
    chat.insert(END, "\n")
    chat.config(state=DISABLED)
    chat.see(END)

if __name__=="__main__":
    root = Tk()
    root.title("Paired Programming")

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
    entry = Entry(chatFrame,bd=5)


    createAvatar()
    createChat()

    root.bind('<Return>', sendMessage)
    root.protocol("WM_DELETE_WINDOW", close_window)


    now = datetime.datetime.now()

    defineFile("VideoLog_" + datetime.datetime.now().strftime("%m") +
     "_" + datetime.datetime.now().strftime("%d") +
     "_" + datetime.datetime.now().strftime("%y"))

    #connect("10.30.146.181", 8080)
    connect("127.0.0.1", 8080)



    receive_msg_thread = Thread(target=listenForMsg)
    receive_msg_thread.daemon = True
    receive_msg_thread.start()


    root.mainloop()


