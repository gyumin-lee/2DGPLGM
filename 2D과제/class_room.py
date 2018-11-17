from pico2d import *

class Class_room:
    def __init__(self):
        self.image = load_image('class_room.jpg')

    def update(self):
        pass

    def draw(self):
        self.image.draw(600,400)
