from pico2d import *
import game_world

class Hall:
    def __init__(self):
        self.image = load_image('hall.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600,400)






