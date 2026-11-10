import random

from pico2d import *
import game_world
import game_framework
from grass import Grass
from bird import Bird


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    grass = Grass()
    game_world.add_oject(grass, 0)
    start_positions = random.sample(range(60, 741), 10)
    for x in start_positions:
        bird = Bird(x, 300)
        game_world.add_oject(bird)


def pause():
    pass


def resume():
    pass


def finish():
    game_world.clear()


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()


