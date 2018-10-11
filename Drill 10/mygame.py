import game_framework
import title_state
import main_state
import pico2d

import start_state

pico2d.open_canvas()
game_framework.run(start_state)
pico2d.close_canvas()
