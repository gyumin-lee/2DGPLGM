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
    x = 0
    y = 0

    for i in range(0, 50+1, 2):
        t = i/100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1]
        clear_canvas()


        if p1[0]>p2[0]:
            moving =0
        else:
            moving =100

        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, moving, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 7
        delay(0.05)

i = 0

points = [(random.randint(0 + 50, KPU_WIDTH - 50), random.randint(0 + 50, KPU_HEIGHT - 50)) for i in range(10)]

while True:
    move_randompoint(points[i - 1], points[i])


    i = (i + 1) % 10








close_canvas()