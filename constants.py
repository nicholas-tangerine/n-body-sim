import os

display_scale = 0.90

#display settings
SCREEN_LENGTH = int(os.get_terminal_size()[0] * display_scale)       # length in chars
SCREEN_HEIGHT = int(os.get_terminal_size()[1] * display_scale)       # height in chars
REFRESH_RATE_HZ = 30

CH_WIDTH_TO_HEIGHT_RATIO = 6/11
CH_MAX_RADIUS = 1

CIRCLE_TOLERANCE = 0.1

BORDER_THRESHOLD = 0 #.5

#physics settings
DIMENSIONS = 3

BODIES = 3
DT = 1e-5
G = 6.67e-11

MIN_MASS = 1e21
MAX_MASS = 1e23

DENSITY = 5.66e15
RADIUS_CONST = 0.02

# coordinate limits in physics sim; display.py handles scaling coordinates to display
MIN_X = -500 
MAX_X = 500

MIN_Y = -500
MAX_Y = 500

MIN_Z = 0
MAX_Z = MAX_X - MIN_X

Z_PRIME = SCREEN_LENGTH / (MAX_X - MIN_X) * MAX_Z 

# restricts the bodies to spawn within the center of coordinate limits. multiplies inital spawn coords by this
INITIAL_POSITION_FACTOR = 0.5
