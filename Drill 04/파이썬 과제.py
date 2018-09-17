from pico2d import *
import math

open_canvas()

os.chdir('D:\\2D게임프로그래밍\\2018-2DGP\\Labs\Lecture03')

grass = load_image('grass.png')
character = load_image('character.png')


while(True):

      x = 0
      y = 0
      i = 0
      j = 0
      d = 0
      z = 0
      r = 0
      while(x<760):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            x = x+2
            delay(0.01)

      while(y<450):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, 90+y)
            y = y+2
            delay(0.01)

      while(i<760):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x-i, 90+y)
            i = i +2
            delay(0.01)

      
      while(d<450):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(0, 90+y-d)
            d = d+2
            delay(0.01)
      
      while(r<360):
            theta = math.radians(1.7)
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(400+x, 300+y)
            y = math.sin(math.radians(z)) * 220
            x = math.cos(math.radians(z)) * 220
            z =z +2
            r = r + 1
            delay(0.01)





close_canvas()
