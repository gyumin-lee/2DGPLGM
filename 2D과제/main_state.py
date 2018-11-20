import random
import json
import os

from pico2d import*
import game_framework
import game_world

from boy import  Boy
from hall import Hall
from library import Library
from class_room import Class_room

name = "MainState"

boy = None

def enter():
    global boy, hall, class_room, libaray
    boy = Boy()
    hall= Hall()
    game_world.add_object(hall, 0)
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

        if boy.x > 800 and boy.y <400:
            boy.image = load_image('library.png')

def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()
