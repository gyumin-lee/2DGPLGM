from pico2d import *

class Music_room:
    def __init__(self):
        self.image = load_image('music_room.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)
