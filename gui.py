
from tkinter import *

def createAvatar():
    # replace this with an avatar widget
    avatar = Label(avatarFrame,text = "avatar") # replace this with the image of the avatar
    avatar.pack()

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
avatarFrame.grid(row=0, column=0,sticky="NSEW")
chatFrame.grid(row=1, column=0,sticky="NSEW")
avatarFrame.pack(fill=BOTH, expand=1) #frame will change size as well if window size is changed
chatFrame.pack(fill=BOTH,expand=1) #frame will change size as well if window size is changed
entry = Entry(chatFrame,bd=5)


createAvatar()
createChat()

root.mainloop()


