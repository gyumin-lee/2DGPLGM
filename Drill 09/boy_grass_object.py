from pico2d import *
import random

# Game object class here
class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')


    def update(self):
        self.frame = (self.frame+1)%8
        self.x += 5

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



# initialization code
open_canvas()

team = [Boy() for i in range(11)]
grass = Grass()

running =True;
# game main loop code
while running:
    handle_events()

for boy in team:
    boy.update()

    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

self.frame = random.randint0,7)
    delay(0.05)

# finalization code
