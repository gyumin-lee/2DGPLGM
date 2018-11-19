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
RIGHT_DOWN, LEFT_DOWN, UP_DOWN, DOWN_DOWN, RIGHT_UP, LEFT_UP, UP_UP, DOWN_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYUP, SDLK_SPACE): SPACE
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
        boy.x += boy.velocityX * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1200 - 25)
        boy.y += boy.velocityY * game_framework.frame_time
        boy.y = clamp(25, boy.y, 800 - 25)

    @staticmethod
    def draw(boy):
            if boy.dirX == 1:
                boy.image.clip_draw(0, 56, 50, 56, boy.x, boy.y)
            elif boy.dirY == 1:
                boy.image.clip_draw(0, 0, 50, 56, boy.x, boy.y)
            elif boy.dirX == -1:
                boy.image.clip_draw(0, 112, 50, 56, boy.x, boy.y)
            elif boy.dirY == -1:
                boy.image.clip_draw(0, 168, 50, 56, boy.x, boy.y)



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

        boy.dirX = clamp(-1, boy.velocityX, 1)
        boy.dirY = clamp(-1, boy.velocityY, 1)


    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.Do_Read()

    @staticmethod
    def do(boy):
        boy.count += 1
        if boy.count == 5:
            boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            boy.count = 0

        boy.x += boy.velocityX * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1200 - 25)
        boy.y += boy.velocityY * game_framework.frame_time
        boy.y = clamp(25, boy.y, 800 - 25)


    @staticmethod
    def draw(boy):
        if boy.dirX == 1:
            boy.image.clip_draw(int(boy.frame) * 50, 56, 50, 56, boy.x, boy.y)
        elif boy.dirY == 1:
            boy.image.clip_draw(int(boy.frame) * 50, 0, 50, 56, boy.x, boy.y)
        elif boy.dirX == -1:
            boy.image.clip_draw(int(boy.frame) * 50, 112, 50, 56, boy.x, boy.y)
        elif boy.dirY == -1:
            boy.image.clip_draw(int(boy.frame) * 50, 168, 50, 56, boy.x, boy.y)

textGroup = Do_Read.TextGroup()

class TalkState:
    @staticmethod
    def enter(boy,event):
        pass

    @staticmethod
    def do(boy):
        boy.count += 1
        if boy.count == 5:
            boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            boy.count=0


        boy.x += boy.velocityX * game_framework.frame_time
        boy.y += boy.velocityY * game_framework.frame_time


    @staticmethod
    def exit(boy,event):
        if event == SPACE:
            boy.Do_Read()

    @staticmethod
    def draw(boy):
            if boy.dirX == 1:
                boy.image.clip_draw(int(boy.frame) * 50, 56, 50, 56, boy.x, boy.y)
            elif boy.dirY == 1:
                boy.image.clip_draw(int(boy.frame) * 50, 0, 50, 56, boy.x, boy.y)
            elif boy.dirX == -1:
                boy.image.clip_draw(int(boy.frame) * 50, 112, 50, 56, boy.x, boy.y)
            elif boy.dirY == -1:
                boy.image.clip_draw(int(boy.frame) * 50, 168, 50, 56, boy.x, boy.y)
            textGroup.draw(boy)

next_state_table = {
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, SPACE: TalkState},
    TalkState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, UP_UP: IdleState, DOWN_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, SPACE: IdleState},
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, UP_UP: RunState, DOWN_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, SPACE: TalkState}
}
class Boy:

    def __init__(self):
        self.x, self.y = 600, 400
        self.image = load_image('character.png')
        self.velocityX = 0
        self.velocityY = 0
        self.dirX = 0
        self.dirY = 1
        self.frame = 0
        self.count = 0
        self.event_que = []
        self.cur_state = IdleState
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
