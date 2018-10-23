from pico2d import*

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

frame = 1
x = 0

while True:
    while x<800:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame*100, 100, 100, 100, x, 90)
        frame = (frame+1) % 8
        update_canvas()
        x += 5
        delay(0.05)
        get_events()
        clear_canvas()

    while x>0:
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        frame = (frame + 1) % 8
        update_canvas()
        x -= 5
        delay(0.05)
        get_events()
        clear_canvas()

