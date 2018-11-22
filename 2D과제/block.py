from pico2d import *
import game_world

class block:
    def __init__(self, x, y , sub_x, sub_y):
        self.image = None
        self.x = x
        self.y = y
        self.sub_x = sub_x
        self.sub_y = sub_y

    def update(self):
        pass

    def get_bb(self):
        return self.x - self.sub_x, self.y - self.sub_y, self.x + self.sub_x, self.y+self.sub_y

    def draw(self):
        pass







