import game_framework
import pico2d

pico2d.open_canvas(1200, 800)
import main_state


game_framework.run(main_state)
pico2d.close_canvas( )