# Driver to test Avatar_widget in separate window

from tkinter import *
from tkinter import ttk

from avatar_util import Avatar_state
from avatar import Avatar_widget

if __name__ == "__main__":

    root = Tk()
    root.title("Test_Avatar")

    avatar = Avatar_widget(root).grid()
    root.mainloop()


