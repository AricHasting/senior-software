from avatar import Avatar_widget
from tkinter import *

avatar_state_var = None

def createAvatar():
    avatar = Avatar_widget(avatarFrame)
    global avatar_state_var 
    avatar_state_var = avatar.get_state_var()

def createChat():
    # replace this with a chat widget
    chatString = "chat"
    chat = Message(chatFrame,text = chatString, width = (windowWidth - (0.1*windowWidth)))

    chat.pack()

    send = Button(chatFrame,text="send", command=sendMessage)
    send.pack(side=BOTTOM)
    entry.pack(side = BOTTOM)


def sendMessage():
    print("This would have sent %s if it was implemented." % entry.get()) # send message here instead of printing
    entry.delete(first=0,last="end") # clear the entry


root = Tk()
root.title("Paired Programming")

# can change the size if necessary
windowWidth = 200
windowHeight = 400

size = str(windowWidth) + "x" + str(windowHeight)
root.geometry(size)

# the colors are just there to differentiate the frames, should change later
avatarFrame = Frame(root, bg = "red",width=windowWidth, height=windowHeight/2, bd=5)
chatFrame = Frame(root, bg="blue", width=windowWidth, height=windowHeight/2, bd=5)
avatarFrame.pack(fill=BOTH, expand=1)
chatFrame.pack(fill=BOTH,expand=1)
entry = Entry(chatFrame,bd=5)


createAvatar()
createChat()

root.mainloop()


