# define types used by avatar widget

from abc import ABC, abstractmethod
from enum import Enum

class Avatar_state(Enum):
    NEUTRAL = "neutral"
    HAPPY = "happy"
    CONFUSED = "confused"
    SAD = "sad"
    DIZZY = "dizzy"
   #EARTH
   #WATER
   #FIRE
   #AIR

# Dictionary of video paths for each state:
video_paths = {
        Avatar_state.NEUTRAL:"videos/Neutral.webm",
        Avatar_state.HAPPY:"videos/Happy.webm",
        Avatar_state.CONFUSED:"videos/Confused.webm",
        Avatar_state.SAD:"videos/Sad_paper.webm",
        Avatar_state.DIZZY:"videos/Dizzy.webm"
        }
