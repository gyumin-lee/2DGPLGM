from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def move_randompoint(p1, p2):
    global x, y
    global frame
    global moving

    frame =0
    moving = 100
    x = 25
    y = 50

    for i in range(0,50+1, 2):
        t = i/100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1]
        clear_canvas()

        



kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
update_canvas()

close_canvas()