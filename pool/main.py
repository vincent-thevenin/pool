import pygame

import collisions
import event
import gamestate
import graphics
import config

from time import sleep

from matplotlib import pyplot as plt
import numpy as np
from math import cos, sin, pi

from multiprocessing import Pool
import os
from tqdm import tqdm

num_thread = 4*4
num_episodes = 100

#region def playgame
def play_game(game_idx):
    was_closed = False
    step = 0
    if not os.path.isdir(str(game_idx)):
        os.mkdir(str(game_idx))
    while not was_closed:
        game = gamestate.GameState()
        button_pressed = config.play_game_button #graphics.draw_main_menu(game)

        if button_pressed == config.play_game_button:
            game.start_pool()
            events = event.events()
            while not (events["closed"] or game.is_game_over or events["quit_to_main_menu"] or step==10):
                print(step)
                events = event.events()
                collisions.resolve_all_collisions(game.balls, game.holes, game.table_sides)
                game.redraw_all()
                
                table = np.zeros((config.resolution[0], config.resolution[1]))
                for i in range(len(list(game.balls))):
                    pos = list(game.balls)[i].ball.pos
                    table[
                        [int(pos[0] + cos(i*2*pi/360)*12.5) for i in range(360)],
                        [int(pos[1] + sin(i*2*pi/360)*12.5) for i in range(360)]
                    ] = 1

                plt.imshow(table, cmap='gray')
                plt.savefig(str(game_idx) + '/'+str(step)+'.png')
                step += 1


                if game.all_not_moving():
                    game.check_pool_rules()
                    game.cue.make_visible(game.current_player)
                    while not (
                        (events["closed"] or events["quit_to_main_menu"]) or game.is_game_over) and game.all_not_moving():
                        game.redraw_all()
                        events = event.events()
                        if True: #game.cue.is_clicked(events):
                            game.cue.cue_is_active(game, events)
                        elif game.can_move_white_ball and game.white_ball.is_clicked(events):
                            game.white_ball.is_active(game, game.is_behind_line_break())
            was_closed = True #events["closed"]

        if button_pressed == config.exit_button:
            was_closed = True

    print('closing')
    pygame.quit()
    print('done')
#endregion

def play_game2(game_idx):
    os.system('python pool/pool/main2.py '+str(game_idx))

with Pool(num_thread) as p:
    #list(tqdm(p.map(play_game2, list(range(num_episodes)))))
    list(tqdm(p.map(play_game2, [71])))



print('donedone')