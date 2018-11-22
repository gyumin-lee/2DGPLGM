import random
import json
import os

from pico2d import*
import game_framework
import game_world


from boy import  Boy
from hall import Hall
from block import block

name = "MainState"


boy = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global boy, hall, block
    boy = Boy()
    hall= Hall()
    #block = block(258, 97, 258, 97)
    block = block(245, 570, 245, 180)
    game_world.add_object(hall, 0)
    game_world.add_object(block, 0)
    game_world.add_object(boy, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(boy,block):
       boy.stop()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()
