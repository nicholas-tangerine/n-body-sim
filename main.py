import phys
from phys import Physics
from display import Display
import time

DT = phys.DT
BODIES = phys.BODIES
DIMENSIONS = phys.DIMENSIONS

SCREEN_LENGTH = 50
SCREEN_HEIGHT = 25
REFRESH_RATE_HZ = 50

physics = Physics()
display = Display()


while True:

    physics.update_accel()
    physics.update_velocity()
    physics.update_coords()

    coords = physics.get_coords()

    display.update_screen(coords)
    display.display_screen()

    time.sleep(1 / REFRESH_RATE_HZ)

