from src import constants

from src.phys import Physics
from src.display import Display
import time

DT = constants.DT
BODIES = constants.BODIES
DIMENSIONS = constants.DIMENSIONS

REFRESH_RATE_HZ = constants.REFRESH_RATE_HZ

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

