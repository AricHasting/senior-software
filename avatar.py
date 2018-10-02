# agent avatar module

import cv2
from tkinter import *
from tkinter import ttk

from avatar_util import Avatar_state

# Avatar widget
class Avatar_widget(ttk.Label):
    #For now, hard code image file paths
    #TODO code file paths
    video_paths = {
            Avatar_state.NEUTRAL:"images/neutral.gif",
            Avatar_state.HAPPY:"images/happy.gif",
            Avatar_state.SAD:"images/sad.gif",
            Avatar_state.CONFUSED:"images/confused.gif"
            }

    # Constructor
    # Automatically set initial state to neutral
    def __init__(self, parent):
        self.images = {}
        self.state_str = StringVar()
        #Start in neutral stare
        self.state_str.set(Avatar_state.NEUTRAL.value)
        self.curr_state = Avatar_state(self.state_str.get())
        #Load image files
        for state, video_path in self.video_paths.items():
            self.images[state] = PhotoImage(file=video_path)
        #Call Super Constructor
        ttk.Label.__init__(self, parent, 
                text = self.state_str.get(), image = self.images[self.curr_state])
    # Accessor method for state variable. Returns StringVar object
    def get_state_var(self):
        return self.state_str

    # Updates displayed image and text based on current value of state_str.
    # If the state_str value is not connected to a valid state, nothing changes.
    def update(self, e):
        try:
            self.curr_state = Avatar_state(self.state_str.get())
            self.configure(text = self.state_str.get())
            self.configure(image = self.images[self.curr_state])
            self.image = self.images[self.curr_state]
        except ValueError:
            pass

# Demo of avatar widget

if __name__ == "__main__":

    root = Tk()
    root.title("Test Avatar")

    avatar = Avatar_widget(root)
    avatar.grid(column=0, row=0)

    state_var = avatar.get_state_var()
    state_select = ttk.Combobox(root, textvariable=state_var)
    state_select['values'] = ("Neutral", "Happy", "Sad", "Confused", "invalid state")
    state_select['state'] = "readonly"
    state_select.set("Happy")
    state_select.bind('<<ComboboxSelected>>', avatar.update)
    state_select.grid(column=0, row=1)

    root.mainloop()
