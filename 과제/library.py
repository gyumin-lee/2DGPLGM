from pico2d import *

class Library:
    def __init__(self):
        self.image = load_image('library.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600, 400)
