# agent avatar module

import cv2
from tkinter import *
from tkinter import ttk
import PIL.Image
import PIL.ImageTk

from avatar_util import Avatar_state

# Avatar widget
class Avatar_widget:
    #For now, hard code video file paths
    video_paths = {
            Avatar_state.NEUTRAL:"videos/Neutral_paper.webm",
            Avatar_state.HAPPY:"videos/Happy_paper.webm",
            Avatar_state.SAD:"videos/Sad_paper.webm",
            Avatar_state.CONFUSED:"videos/Confused_paper.webm"
            }

    # Constructor
    # Automatically set initial state to neutral
    def __init__(self, parent_frame, max_width, max_height):
        self.state_str = StringVar()
        self.parent_frame = parent_frame
        #Start in neutral stare
        self.state_str.set(Avatar_state.NEUTRAL.value)
        self.curr_state = Avatar_state(self.state_str.get())
        # initialize video object
        self.vid = Avatar_capture(Avatar_widget.video_paths[self.curr_state])
        # save max size params
        self.max_width = max_width
        self.max_height = max_height
        # create canvas
        self.canvas = Canvas( parent_frame, width=max_width, height=max_height)
        self.canvas.pack()
        
        # After it is called once, update method will automatically repeat
        self.delay = 15
        self.update()
        
    # Accessor method for state variable. Returns StringVar object
    def get_state_var(self):
        return self.state_str

    # Returns the size of a scaled down version of the 
    # video to fit in the canvas
    # size = (width, height)
    def scale(self, size):
        s = min(self.max_width/size[0],self.max_height/size[1])
        return (int(size[0]*s),int(size[1]*s))

    # Update method to check for state updates
    # and choose next frame to display
    def update(self):
        # check for state updates
        state_update = False
        try:
            old_state = self.curr_state
            self.curr_state = Avatar_state(self.state_str.get())
            state_update = old_state != self.curr_state
        except ValueError:
            pass
        # if state is updated, re-initialize Avatar_capture object
        if state_update:
            self.vid = Avatar_capture(Avatar_widget.video_paths[self.curr_state])      
        ret, frame = self.vid.get_frame()
        # if get_frame failed, might be end of video so restart.
        if not ret:
            self.vid = Avatar_capture(Avatar_widget.video_paths[self.curr_state])
            ret, frame = self.vid.get_frame()
        if ret:
            im = PIL.Image.fromarray(frame)
            im.thumbnail(self.scale(im.size))
            self.photo = PIL.ImageTk.PhotoImage(image = im)
            self.canvas.create_image(0,0, image=self.photo, anchor = NW)

        self.parent_frame.after(self.delay, self.update)

class Avatar_capture:
    def __init__(self, video_source):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open avatar video source", video_source)
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Demo of avatar widget

if __name__ == "__main__":

    root = Tk()
    root.title("Test Avatar")

    avatar = Avatar_widget(root,1000,600) 

    state_var = avatar.get_state_var()
    state_select = ttk.Combobox(root, textvariable=state_var)
    state_select['values'] = ("Neutral", "Happy", "Sad", "Confused", "invalid state")
    state_select['state'] = "readonly"
    state_select.set("Happy")
    state_select.pack()

    root.mainloop()
