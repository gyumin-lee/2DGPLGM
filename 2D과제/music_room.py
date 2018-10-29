from pico2d import *

class Library:
    def __init__(self):
        self.image = load_image('음악실.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
