import time

import constants

from display import Display
from particle import Particle

SCREEN_LENGTH = constants.SCREEN_LENGTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT

DIMENSIONS = constants.DIMENSIONS

MIN_X = constants.MIN_X
MAX_X = constants.MAX_X

MIN_Y = constants.MIN_Y
MAX_Y = constants.MAX_Y

MIN_Z = constants.MIN_Z
MAX_Z = constants.MAX_Z

Z_PRIME = constants.Z_PRIME

CH_MAX_RADIUS = constants.CH_MAX_RADIUS

class DisplayParticles:
    def __init__(self):
        """Initialize display wrapper for particles"""
        self.display = Display()

    def _scale_to_xy_plane(self, coord, radius = None):
        """
        MODIFIES coord IN PLACE
        Scales 2d coords to scale. Scales 3d coords to scale based on distance

        Args: 
            List[int] coord:        x,y or x,y,z coordinates
            (optional) int radius:  radius of circle

        Returns: 
            int:                the radius in character lengths
        """

        coord[0] = round((coord[0] - MIN_X) * SCREEN_LENGTH / (MAX_X - MIN_X))
        coord[1] = round((coord[1] - MIN_Y) * SCREEN_HEIGHT / (MAX_Y - MIN_Y))

        if len(coord) > 3:
            raise Exception("coords has too many dimensions")

        if len(coord) == 3:
            scaling_factor = Z_PRIME / coord[2]#coord[2] / Z_PRIME

            coord[0] = round(coord[0] * scaling_factor)
            coord[1] = round(coord[1] * scaling_factor)

            radius = min(round(radius * scaling_factor), CH_MAX_RADIUS)
            radius = max(1, radius)

        return radius

    def draw_particle(self, particle):
        coords = particle.get_coords()
        radius = particle.get_radius()

        radius = self._scale_to_xy_plane(coords, radius)

        self.display.add_circle(coords, radius)

    def draw_particle_system(self, particles):
        for particle in particles:
            self.draw_particle(particle)

    def clrscr(self):
        self.display.wipe_screen()

    def refresh(self):
        self.display.display_screen()
