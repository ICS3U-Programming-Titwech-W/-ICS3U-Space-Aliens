#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: june.9.2022
# program displays "space aliens" in the pybadge 

import ugame
import stage 

import constants


def game_scene():

    # image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state info on 
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"] 

    # get sound ready 
    # pew_sound = open("pew.wav", 'rb')
    # sound = ugame.audio
    #sound.stop()
    #sound.mute(False)


    # set the background to images 0 in the image bank
    # and set the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5 , 75, 66)

    alien = stage.Sprite(image_bank_sprites, 9, 
                     int(constants.SCREEN_X / 2 - constants. SPRITE_SIZE / 2), 16)

    # create a stage fro the background to show up on 
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
                a_button ==  constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button == constants.button_state["button_sill_pressed"]
            else:
                if a_button ==  constants.button_state["button_still_pressed"]:
                    a_button ==  constants.button_state["button_released"]
                else:
                    a_button == constants.button_state["button_up"]

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
            
        # udate game logic

        # redraw sprites
        games.render_sprites([ship] + [alien])
        games.tick()


if __name__ =="__main__":
        game_scene()

