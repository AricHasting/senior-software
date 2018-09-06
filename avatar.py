# agent avatar module

from tkinter import *
from tkinter import ttk

from avatar_util import Avatar_state

# Avatar widget
class Avatar_widget(ttk.Label):
    #For now, hard code image file paths
    #TODO code file paths
    image_paths = {
            Avatar_state.NEUTRAL:"images/neutral.gif",
            Avatar_state.HAPPY:"images/happy.gif",
            Avatar_state.SAD:"images/sad.gif",
            Avatar_state.CONFUSED:"images/confused.gif"
            }

    # Constructor
    # Automatically set initial state to neutral
    def __init__(self, parent):
        self.images = {}
        for state, image_path in self.image_paths.items():
            self.images[state] = PhotoImage(file=image_path)
        #start in neutral state
        iState = Avatar_state.NEUTRAL
        ttk.Label.__init__(self, parent, 
                text = iState.value, image = self.images[state])

    def update(self, state):
        if isinstance(state, Avatar_state):
            self.configure(text = state.value)
            self.configure(image = self.images[state])
            self.image = self.images[state]

# Demo of avatar widget

if __name__ == "__main__":

    root = Tk()
    root.title("Test Avatar")

    avatar = Avatar_widget(root)
    avatar.grid(column=0, row=0)

    state_var = StringVar()
    state_select = ttk.Combobox(root, textvariable=state_var)
    state_select['values'] = ("Neutral", "Happy", "Sad", "Confused")
    state_select['state'] = "readonly"
    state_select.set("Happy")
    state_select.bind('<<ComboboxSelected>>', avatar.update(Avatar_state(state_select.get())))
    state_select.grid(column=0, row=1)

    root.mainloop()
