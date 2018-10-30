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

class Avatar(Enum):
    MALE = "male"
    FEMALE = "female"
    THE_BEST_AVATAR = "paul"

# Dictionaries of video paths for each state:
male_states = {
        Avatar_state.NEUTRAL:"videos/male_neutral.mp4",
        Avatar_state.HAPPY:"videos/male_happy.mp4",
        Avatar_state.CONFUSED:"videos/male_confused.mp4",
        Avatar_state.SAD:"videos/male_sad.mp4",
        Avatar_state.DIZZY:"videos/male_dizzy.mp4"
        }

female_states = {
        Avatar_state.NEUTRAL:"videos/female_neutral.mp4",
        Avatar_state.HAPPY:"videos/female_happy.mp4",
        Avatar_state.CONFUSED:"videos/female_confused.mp4",
        Avatar_state.SAD:"videos/female_sad.mp4",
        Avatar_state.DIZZY:"videos/female_dizzy.mp4"
        }

the_best_states = {
        Avatar_state.NEUTRAL:"videos/paul_neutral.webm",
        Avatar_state.HAPPY:"videos/paul_happy.webm",
        Avatar_state.CONFUSED:"videos/paul_confused.webm",
        Avatar_state.SAD:"videos/paul_sad.webm",
        Avatar_state.DIZZY:"videos/paul_dizzy.webm"
        }

# Dictionary of avatars
video_paths = {
        Avatar.MALE:male_states,
        Avatar.FEMALE:female_states,
        Avatar.THE_BEST_AVATAR:the_best_states
        }
    
