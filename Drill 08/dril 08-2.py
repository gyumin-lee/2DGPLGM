from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')



kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
update_canvas()

close_canvas()