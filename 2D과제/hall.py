from pico2d import *
import game_world

class Hall:
    def __init__(self):
        self.image = load_image('hall.jpg')

    def update(self):
        pass

    def get_bb(self):
        pass


    def draw(self):
        self.image.draw(600,400)


class Block_1:
    def __init__(self):
        if(self.x > 552 and self.x < 554 and self.y > 400 and self.y < 795):
            Block_1
