#!/usr/bin/env python3
 
# Created by: Titwech Wal
# Created on: june.9.2022
# program displays "space aliens" in the pybadge 
 
 
import ugame
import stage 
import time
import random
import supervisor
 
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
    text2.move(5, 30)
    text2.text("Shoot the fire")
    text.append(text2)
 
    text3 = stage.Text(width= 29, height = 12, font = None, palette = constants.RED_PALETTE , buffer=None)
    text3.move(5, 40)
    text3.text("to save you planet.")
    text.append(text3)
 
    text4 = stage.Text(width= 29, height = 12, font = None, palette = constants.RED_PALETTE , buffer=None)
    text4.move(5, 60)
    text4.text("Touch the fire")
    text.append(text4)
 
    text5 = stage.Text(width= 29, height = 12, font = None, palette = constants.RED_PALETTE , buffer=None)
    text5.move(5, 70)
    text5.text("and you DIE!")
    text.append(text5)
 
    text5 = stage.Text(width= 29, height = 12, font = None, palette = constants.RED_PALETTE , buffer=None)
    text5.move(40, 110)
    text5.text("PRESS START")
    text.append(text5)
 
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
            game_scene()
 
        # redraw sprites
        games.tick()
 
def game_scene():
 
    # for the score
    score = 0
 
    score_text = stage.Text(width = 29, height = 14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {}".format(score))
 
 
    def show_alien():
        # this function takes an alien off the screen and moves it on screen 
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants. SPRITE_SIZE, 
                                                         constants.SCREEN_X - constants.SPRITE_SIZE), 
                                          constants.OFF_TOP_SCREEN)
                break
 
    # image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("color_template.bmp")
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
 
    # get sound ready 
    boom_sound = open("boom.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
 
    # get sound ready 
    crash_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
 
 
 
 
    # set the background to images 0 in the image bank
    # and set the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
 
    for x_location in range (constants.SCREEN_GRID_X):
            for y_location in range(constants. SCREEN_GRID_Y):
                tile_picked = random.randint(10,12)
                background.tile(x_location, y_location, tile_picked)
 
 
    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 8 , 75, 100)
 
    alien = stage.Sprite(image_bank_sprites, 9, 
                         int(constants.SCREEN_X / 2 - constants. SPRITE_SIZE / 2), 16)
 
    # Create a list of laser for when we shoot
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
            a_single_alien = stage.Sprite(image_bank_sprites, 6, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
 
            aliens.append(a_single_alien) 
    # put one alien on the screen
    show_alien()
 
    # Create a list of laser for when we shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
            a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
 
            lasers.append(a_single_laser)
 
 
    # create a stage for the background to show up on 
    # set frame rate tp 60fps
    games = stage.Stage(ugame.display, constants.FPS)
 
    #set all layers of sprites, items show up in order 
    games.layers =  [score_text] + aliens + lasers + [ship] + [background]
 
    #render all sprites 
    # most likey you'll only render the background once per game 
    games.render_block()
 
    # repeate forever
    while True: 
        # when butten are pressed this will extcute 
        keys  = ugame.buttons.get_pressed()
 
        # A button pressed
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button =  constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
 
                # fire a laser if we have enough power (have not used up all the lasers)
                for laser_number in range(len(lasers)):
                    if lasers[laser_number].x < 0:
                        lasers[laser_number].move(ship.x, ship.y)
                        sound.play(pew_sound)
                        break                
 
            else:
                if a_button ==  constants.button_state["button_still_pressed"]:
                    a_button =  constants.button_state["button_released"]
                else:
                    a_button = constants.button_state["button_up"]
 
        # pass will make sure nothing happens when button is pressed
        if keys & ugame.K_X:
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
 
        
        # each frame move the laser, that have been fired up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
 
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
 
        
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
 
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, 
                                              constants.OFF_SCREEN_Y)
 
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                        score_text.clear()
                        score_text.cursor(0, 0)
                        score_text.move(1, 1)
                        score_text.text("Score: {}".format(score))
 
        # each fram check if any if the lasers are touching any aliens 
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x + 6, lasers[laser_number].y + 2,
                                         lasers[laser_number].x + 11, lasers[laser_number].y + 12,
                                         aliens[alien_number].x + 1, aliens[alien_number].y,
                                         aliens[alien_number].x + 15, aliens[alien_number].y + 15):
                            # laser hits an alien
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            show_alien()
                            show_alien()
                            score = score + 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {}".format(score))
 
        #each frame check if any aliens are touching the space ship
       
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    # aline hit the ship
                    sound.stop()
                    sound.play(crash_sound)
                    time.sleep(3.0)
                    game_over_screen(score)
 
        # redraw sprite list
        games.render_sprites(lasers + [ship] + aliens)
        games.tick()
 
    
 
             
 
 
def game_over_screen(final_score):
    
    # turn off sound from the last scene
    sound = ugame.audio
    sound.stop()
 
    # image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
 
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
 
 
    # add text objects 
    text = []
    text1 = stage.Text(width= 29, height = 14, font = None, palette = constants.RED_PALETTE , buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2}".format(final_score))
    text.append(text1)
 
    text2 = stage.Text(width= 29, height = 14, font = None, palette = constants.RED_PALETTE , buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)
 
    text3 = stage.Text(width= 29, height = 14, font = None, palette = constants.RED_PALETTE , buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)
 
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
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()
 
        # redraw sprites
        games.tick()
 
 
if __name__ =="__main__":
        splash_scene()
 

