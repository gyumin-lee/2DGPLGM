from pico2d import *

class Hall:
    def __init__(self):
        self.image = load_image('hall.jpg')

    def update(self, boy):
        pass

    def draw(self):
        self.image.draw(600,400)
