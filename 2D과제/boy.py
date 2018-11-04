from pico2d import *
import game_framework

import game_world
import Do_Read

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

# Boy Event
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, SPACE, GAME_TIMER = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States
class IdleState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityX += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocityX -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityY += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityY -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocityX -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocityX += RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocityY -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocityY += RUN_SPEED_PPS


    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.Do_Read()


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4




    @staticmethod
    def draw(boy):
        if boy.velocityX == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 50, 56, boy.x, boy.y)
        elif boy.velocityY == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 60, 50, 56, boy.x, boy.y)
        elif boy.velocityX == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 120, 50, 56, boy.x, boy.y)
        elif boy.velocityY == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 180, 50, 56, boy.x, boy.y)
class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityX += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocityX -= RUN_SPEED_PPS
        elif event == UP_DOWN:
            boy.velocityY += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            boy.velocityY -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocityX -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocityX += RUN_SPEED_PPS
        elif event == UP_UP:
            boy.velocityY -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            boy.velocityY += RUN_SPEED_PPS


    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.Do_Read()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 4
        boy.x += boy.velocityX * game_framework.frame_time
        boy.y += boy.velocityY * game_framework.frame_time


    @staticmethod
    def draw(boy):
        if boy.velocityX == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 50, 56, boy.x, boy.y)
        elif boy.velocityY == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 60, 50, 56, boy.x, boy.y)
        elif boy.velocityX == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 120, 50, 56, boy.x, boy.y)
        elif boy.velocityY == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 180, 50, 56, boy.x, boy.y)

textGroup = Do_Read.TextGroup()

class TalkState:
    @staticmethod
    def enter(boy,event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 4
        boy.x += boy.velocityX * game_framework.frame_time
        boy.y += boy.velocityY * game_framework.frame_time


    @staticmethod
    def exit(boy,event):
        if event == SPACE:
            boy.Do_Read()

    @staticmethod
    def draw(boy):
        if boy.velocityX == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 50, 56, boy.x, boy.y)
        elif boy.velocityY == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 60, 50, 56, boy.x, boy.y)
        elif boy.velocityX == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 120, 50, 56, boy.x, boy.y)
        elif boy.velocityY == -1:
            boy.image.clip_draw(int(boy.frame) * 100, 180, 50, 56, boy.x, boy.y)
        textGroup.draw(boy)

next_state_table = {
    RunState: {RIGHT_UP: RunState, LEFT_UP: IdleState, UP_UP: RunState, DOWN_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, SPACE: TalkState},
    TalkState: {RIGHT_UP: TalkState, LEFT_UP: TalkState, UP_UP: TalkState, DOWN_UP: TalkState, LEFT_DOWN: TalkState, RIGHT_DOWN: TalkState, UP_DOWN: TalkState, DOWN_DOWN: TalkState, SPACE: RunState},
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP: RunState, DOWN_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, SPACE: TalkState}
}
class Boy:

    def __init__(self):
        self.x, self.y = 600, 400
        self.image = load_image('character.png')
        self.velocityX = 1
        self.velocityY = 1
        self.dirX = 1
        self.dirY = 1
        self.frame = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def Do_Read(self):
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
