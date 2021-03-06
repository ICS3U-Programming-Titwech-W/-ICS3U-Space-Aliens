#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: june.9.2022
# program has the constants for space aliens 

# pybadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 1
ALIEN_SPEED = 1
OFF_SCEEN_X = -100
OFF_SCEEN_Y = -100 
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTON_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60
SPRITE_MOVMENT_SPEED = 1

# using button state 
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released":"released"
}

# new pallet for filled text
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')