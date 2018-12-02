import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# monster Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# monster Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

class Monster:
    def __int__(self):
        self.x, self.y = 200, 600
        self.frame = 0
        self.image = load_image('monster.png')
        self.dirX = 0
        self.dirY = 1

    def get__bb(self):
        return self.x -30, self.y-30, self.x +30, self.y+30

    def update(self):
        self.x += self.dirX
        self.y += self.dirY
        if self.x >= 600:
            self.dirX = -1
        elif self.x <= 0:
            self.dirX = 1

        if self.y >=400:
            self.dirY = 1
        elif self.y<=0:
            self.dirY =-1

    def draw(self):
        draw_rectangle(*self.get_bb())
        print(self.x, self.y)


