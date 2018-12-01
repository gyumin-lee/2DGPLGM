import random
import json
import os

from pico2d import*
import game_framework
import game_world


from boy import  Boy
from hall import Hall
from monster import Monster
from block import Block



name = "MainState"


boy = None
monster = None

def get_boy():
    return boy

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def enter():
    global boy, block, block1, block2, block3
    global monster
    monster = Monster()
    game_world.add_object(monster, 1)
    boy = Boy()
    hall= Hall()

    block = Block(258, 97, 258, 97)
    block1 = Block(245, 570, 245, 180)
    block2 = Block(937, 611, 270, 215)
    block3 = Block(945, 106, 228, 70)

    game_world.add_object(hall, 0)
    game_world.add_object(block, 0)
    game_world.add_object(block1, 0)
    game_world.add_object(block2, 0)
    game_world.add_object(block3, 0)
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
    if collide(boy, block):
        boy.stop()
    if collide(boy, block1):
        boy.stop()
    if collide(boy, block2):
        boy.stop()
    if collide(boy, block3):
        boy.stop()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()
