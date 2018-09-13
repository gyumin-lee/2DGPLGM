from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
s = 0
while (True):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * s, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    if (x > 800):
        s = 0
    elif (x < 0):
        s = 1

    if (s == 1):
        x += 10
    elif (s == 0):
        x -= 10

    delay(0.05)
    get_events()


close_canvas()

