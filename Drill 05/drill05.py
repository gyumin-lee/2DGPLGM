from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_203_535():
    x, y = 800 // 2, 90
    frame = 0

    while (x > 203 and y < 535):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        y += 5
        delay(0.05)
        get_events()

def move_132_243():
    pass

def move_535_470():
    pass

def move_477_203():
    pass

def move_715_136():
    pass

def move_316_225():
    pass

def move_510_92():
    pass

def move_692_518():
    pass

def move_682_336():
    pass

def move_712_349():
    pass




while True:
    move_203_535()
    move_132_243()
    move_535_470()
    move_477_203()
    move_715_136()
    move_316_225()
    move_510_92()
    move_692_518()
    move_682_336()
    move_712_349()


