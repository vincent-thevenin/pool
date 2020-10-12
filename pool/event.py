import numpy as np
import pygame
import random


class GameEvent():
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data


def set_allowed_events():
    # only allow keypress events to avoid waisting cpu type on checking useless events
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

def events():
    closed = False
    quit = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit = True

    return {"quit_to_main_menu": quit,
            "closed": closed,
            "clicked": random.random()<0.5,#pygame.mouse.get_pressed()[0],
            "mouse_pos": np.zeros(2) #np.random.randint(100, 500, (2)) #np.array(pygame.mouse.get_pos())
            }
