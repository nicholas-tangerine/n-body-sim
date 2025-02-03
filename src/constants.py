import os

display_scale = 0.95

#display settings
SCREEN_LENGTH = int(os.get_terminal_size()[0] * display_scale)       # length in chars
SCREEN_HEIGHT = int(os.get_terminal_size()[1] * display_scale)       # height in chars

REFRESH_RATE_HZ = 50

#physics settings
DIMENSIONS = 2

BODIES = 11
DT = 1e-5
G = 6.67e-11

MIN_MASS = 1e21
MAX_MASS = 1e23

# coordinate limits in physics sim; display.py handles scaling coordinates to display
MIN_X = -500
MAX_X = 500
MIN_Y = -500
MAX_Y = 500

# restricts the bodies to spawn within the center of coordinate limits. multiplies inital spawn coords by this
INITIAL_POSITION_FACTOR = 0.5
