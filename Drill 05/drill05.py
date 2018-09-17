from pico2d import *

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
        x -= 1.3
        y += 3
        delay(0.05)
        get_events()

def move_132_243():
    x, y = 203, 535
    frame=0

    while (x > 132 and y > 243):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        y -= 5
        delay(0.05)
        get_events()

def move_535_470():
    x, y = 132, 243
    frame =0

    while (x < 535 and y <470):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 3
        y += 6
        delay(0.05)
        get_events()

def move_477_203():
    x, y = 535, 470
    frame =0

    while (x > 477 and y > 203 ):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 1
        y -= 4
        delay(0.05)
        get_events()



def move_715_136():
    x, y = 477, 203
    frame =0

    while (x < 716 and y  > 136 ):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 3
        y -= 1
        delay(0.05)
        get_events()




def move_316_225():
    x, y = 715, 136
    frame =0

    while (x > 316 and y  < 225 ):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        y += 1
        delay(0.05)
        get_events()



def move_510_92():
    x, y = 316, 225
    frame =0
    while (x < 510 and y  > 92 ):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 3.6
        y -= 2
        delay(0.05)
        get_events()

def move_692_518():
    x, y =510, 92
    frame =0

    while (x < 692 and y  < 518 ):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 1
        y += 4
        delay(0.05)
        get_events()

def move_682_336():
    pass

def move_712_349():
    pass




while True:
    # move_203_535()
    # move_132_243()
    # move_535_470()
    # move_477_203()
    # move_715_136()
    # move_316_225()
    # move_510_92()
    move_692_518()
    move_682_336()
    move_712_349()


