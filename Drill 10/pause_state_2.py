import game_framework
from pico2d import *
import main_state
import title_state

name = "PauseState_2"
image = None


class Pause:
    def __init__(self):
        self.image = load_image('pause_2.png')
        self.switch = 0

    def draw(self):
        if self.switch == 1:
            self.image.draw(400, 300)

    def update(self):
        self.switch = (self.switch + 1) % 5
        delay(0.05)

def enter():
    global image
    image = Pause()

def exit():
    global image
    del(image)

