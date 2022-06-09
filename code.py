#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: june.9.2022
# program displays "space aliens" in the pybadge 

import ugame
import stage 

def game_scene():

    # image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # set the background to images 0 in the image bank
    # and set the size (10x8 tiles of size 16x16)
    background = stage.grid(image_bank_background, 10, 8)

    # create a stage fro the background to show up on 
    # set frame rate tp 60fps
    games = stage.Stage(ugame.display, 60)

    #render all sprites 
    # most likey you'll only render the background once per game 
    game.render_block()

    # repeate forever
    while true 
        pass #just aplace holder 


if __name__ =="__main__":
        game_scene()

