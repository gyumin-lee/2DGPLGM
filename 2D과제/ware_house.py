from pico2d import *

class Ware_house:
    def __init__(self):
        self.image = load_image('ware_house.jpg')

    def event(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(600,400)
