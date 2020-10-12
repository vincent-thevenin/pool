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

import argparse
import pickle

mydpi = 96

def play_game(game_idx):
    was_closed = False
    global_step = 0
    local_step = 0
    turn = 0
    tmp_list = [[]]
    """fig = plt.figure(figsize=(config.resolution[1]/mydpi, config.resolution[0]/mydpi), dpi=mydpi)
    ax = plt.Axes(fig, [0., 0., 1., 1.])"""

    if not os.path.isdir('dataset/'+str(game_idx)):
        os.mkdir('dataset/'+str(game_idx))
        #os.mkdir('dataset/'+ str(game_idx) + '/' + str(turn))
    while not was_closed:
        game = gamestate.GameState()
        button_pressed = config.play_game_button #graphics.draw_main_menu(game)

        if button_pressed == config.play_game_button:
            game.start_pool()
            events = event.events()
            while not (events["closed"] or game.is_game_over or events["quit_to_main_menu"] or global_step==50000):
                events = event.events()
                collisions.resolve_all_collisions(game.balls, game.holes, game.table_sides)
                game.redraw_all()
                #table = np.zeros((config.resolution[0], config.resolution[1]))
                for i in range(len(list(game.balls))):
                    pos = list(game.balls)[i].ball.pos
                    tmp_list[-1].append(pos.copy())
                    """table[
                        [int(pos[0] + cos(i*2*pi/360)*12.5) for i in range(360)],
                        [int(pos[1] + sin(i*2*pi/360)*12.5) for i in range(360)]
                    ] = 1"""

                tmp_list.append([])
                """ax.set_axis_off()
                fig.add_axes(ax)
                ax.imshow(table, cmap='gray')
                plt.savefig('dataset/'+ str(game_idx) + '/' + str(turn) + '/'+str(local_step)+'.png')
                plt.cla()
                plt.clf()"""
                global_step += 1
                local_step += 1
                


                if game.all_not_moving():
                    if global_step != 1:
                        with open('dataset/'+ str(game_idx) + '/' + str(turn) + '_'+str(local_step)+'.pickle', "wb") as f:
                            pickle.dump(tmp_list[:-1], f)
                            tmp_list = [[]]
                        turn += 1
                        #os.mkdir('dataset/'+ str(game_idx) + '/' + str(turn))
                    local_step = 0
                    game.check_pool_rules()
                    game.cue.make_visible(game.current_player)
                    while not (
                        (events["closed"] or events["quit_to_main_menu"]) or game.is_game_over) and game.all_not_moving():
                        game.redraw_all()
                        events = event.events()
                        if True: #game.cue.is_clicked(events):
                            game.cue.cue_is_active(game, events, global_step==1)
                        elif game.can_move_white_ball and game.white_ball.is_clicked(events):
                            game.white_ball.is_active(game, game.is_behind_line_break())
            was_closed = True #events["closed"]

        if button_pressed == config.exit_button:
            was_closed = True

    print('closing')
    pygame.quit()
    print('done')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_number', type=int)
    args = parser.parse_args()

    
    play_game(args.file_number)