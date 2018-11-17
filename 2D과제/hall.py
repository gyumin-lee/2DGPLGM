from pico2d import *

class Hall:
    def __init__(self):
        self.image = load_image('hall.jpg')

    def event(self):
        pass

    def update(self, boy):
        if(boy.x >=538 and boy.y == 794):
            game_framework.change_state(library)

    def draw(self):
        self.image.draw(600,400)
