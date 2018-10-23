from pico2d import*

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def handle_event():
    global x, y
    global running

x =400
y =90
def Move_203_535():
    if(x>=203 and y <535):


def Move_132_243():

def Move_535_472():

def Move_477_203():

def Move_715_136():

def Move_316_225():

def Move_510_92():

def Move_692_518();

def Move_682_336():

def Move_712_349():





running = True
frame = 0
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    update_canvas()
    frame = (frame + 1) % 8
    Move_203_535()
    Move_132_243()
    Move_535_472()
    Move_477_203()
    Move_715_136()
    Move_316_225()
    Move_510_92()
    Move_692_518()
    Move_682_336()
    Move_712_349()
    handle_event()








