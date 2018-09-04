# agent avatar module

from tkinter import *
from tkinter import ttk

from avatar_util import Avatar_state

# Avatar widget
class Avatar_widget(ttk.Label):
    #For now, hard code image file paths
    #TODO code file paths
    image_list = []
    text_list = {
            Avatar_state.NEUTRAL:"Neutral",
            Avatar_state.HAPPY:"Happy",
            Avatar_state.CONFUSED:"Confused",
            Avatar_state.SAD:"Sad"
    }
    # Constructor
    # Automatically set initial state to neutral
    def __init__(self, parent):
        ttk.Label.__init__(self, parent, 
                text = self.text_list[Avatar_state.NEUTRAL])

    def update(self, state):
        if isinstance(state, Avatar_state):
            self['text'] = text_list[state]

