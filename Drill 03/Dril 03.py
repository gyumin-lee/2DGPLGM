from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
r = 270
while (True):
    while (x < 770):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x +2
        delay(0.01)


    while(y < 560 ):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(770, y)
        y = y +2
        delay(0.01)

    while(x>30):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 560)
        x = x-2
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(32,  y)
        y = y - 2
        delay(0.01)

    while(x<=400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    while (r < 630):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x = 400 + 213 * math.cos(math.radians(r))
        y = 300 + 213 * math.sin(math.radians(r))

        r = r + 1
        delay(0.01)






close_canvas()
