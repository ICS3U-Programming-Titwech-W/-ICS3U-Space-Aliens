#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: june.9.2022
# program displays "space aliens" in the pybadge 

import ugame
import stage 
import time
import random

import constants

def splash_scene():

    # image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    #get sound fro the coin
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)


    # set the background to images 0 in the image bank
    # and set the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage for the background to show up on 
    # set frame rate tp 60fps
    games = stage.Stage(ugame.display, constants.FPS)

    #set all layers of sprites, items show up in order 
    games.layers = [background]

    #render all sprites 
    # most likey you'll only render the background once per game 
    games.render_block()

    # repeate forever
    while True: 
        # wait 2 seconds 
        time.sleep(2.0)
        menu_scene()


def menu_scene():

    # image bank for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects 
    text = []
    text1 = stage.Text(width= 29, height = 12, font = None, palette = constants.RED_PALETTE , buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width= 29, height = 12, font = None, palette = constants.RED_PALETTE , buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # set the background to images 0 in the image bank
    # and set the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)



    # create a stage for the background to show up on 
    # set frame rate tp 60fps
    games = stage.Stage(ugame.display, constants.FPS)

    #set all layers of sprites, items show up in order 
    games.layers = text + [background]

    #render all sprites 
    # most likey you'll only render the background once per game 
    games.render_block()

    # repeate forever
    while True: 
        # when butten are pressed this will extcute 
        keys  = ugame.buttons.get_pressed()

        # A button to fire 
    
        if keys & ugame.K_START:
            pass

        # redraw sprites
        games.tick()

def game_scene():

    # image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state info on 
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"] 

    # get sound ready 
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    # set the background to images 0 in the image bank
    # and set the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    for x_location in range (constants.SCREEN_GRID_X):
            for y_location in range(constants. SCREEN_GRID_Y):
                tile_picked = random.randint(1, 3)
                background.tile(x_location, y_location, tile_picked)


    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5 , 75, 66)

    alien = stage.Sprite(image_bank_sprites, 9, 
                     int(constants.SCREEN_X / 2 - constants. SPRITE_SIZE / 2), 16)

    # create a stage for the background to show up on 
    # set frame rate tp 60fps
    games = stage.Stage(ugame.display, constants.FPS)

    #set all layers of sprites, items show up in order 
    games.layers = [ship] + [alien] + [background]

    #render all sprites 
    # most likey you'll only render the background once per game 
    games.render_block()

    # repeate forever
    while True: 
        # when butten are pressed this will extcute 
        keys  = ugame.buttons.get_pressed()

        # A button to fire 
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button =  constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                sound.play(pew_sound)
                a_button = constants.button_state["button_still_pressed"]
            else:
                if a_button ==  constants.button_state["button_still_pressed"]:
                    a_button =  constants.button_state["button_released"]
                else:
                    a_button = constants.button_state["button_up"]

        # pass will make sure nothing happens when button is pressed
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            #added borders to the right side 
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)   
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)  
        if keys & ugame.K_LEFT:
            # added borders to the left 
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)   
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass  
            

        # redraw sprites
        games.render_sprites([ship] + [alien])
        games.tick()

if __name__ =="__main__":
        game_scene()

