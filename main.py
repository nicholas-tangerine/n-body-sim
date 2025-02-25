import constants

from phys import Physics
from display_particles import DisplayParticles

import time

DT = constants.DT
BODIES = constants.BODIES
DIMENSIONS = constants.DIMENSIONS

REFRESH_RATE_HZ = constants.REFRESH_RATE_HZ

physics = Physics()
display = DisplayParticles()

while True: 
    display.clrscr()

    physics.update_accel()
    physics.update_velocity()
    physics.update_coords()

    # coords = physics.get_coords()
    particles = physics.get_particles()

    display.draw_particle_system(particles)

    time.sleep(1 / REFRESH_RATE_HZ)
    display.refresh()

