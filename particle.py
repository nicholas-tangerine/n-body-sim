import constants

import math

DIMENSIONS = constants.DIMENSIONS
DENSITY = constants.DENSITY

MIN_X = constants.MIN_X
MAX_X = constants.MAX_X

MIN_Y = constants.MIN_Y
MAX_Y = constants.MAX_Y

MIN_Z = constants.MIN_Z
MAX_Z = constants.MAX_Z

class Particle:
    def __init__(self, mass, coords, v = None, a = None):
        """Initializes a Particle object with mass and coordinates"""

        self.mass = mass

        self.coords = coords
        self.velocity = [0] * DIMENSIONS if not v else v
        self.accel = [0] * DIMENSIONS if not a else a

        self.radius = int(( (3 * mass) / (4 * math.pi * DENSITY) ) ** (1/3))    # mass = density * volume
    
    def set_accel(self, accel_vector):
        """Sets a particle's acceleration vector"""
        self.accel = [mag for mag in accel_vector]

    def update_velocity(self, dt):
        """Updates velocity; v = v_0 + at"""
        for i in range(DIMENSIONS):
            self.velocity[i] += self.accel[i] * dt

    def update_coords(self, dt):
        """Updates coordinates; p = p_0 + vt + 0.5at^2"""

        for i in range(DIMENSIONS):
            self.coords[i] += self.velocity[i] * dt + 0.5 * self.accel[i] * dt * dt

    def gone_forever(self):
        """Returns if a particle is gone forever :("""
        vel = self.get_velocity()
        coord = self.get_coords()

        x = coord[0]
        vel_x = vel[0]
        
        y = coord[1]
        vel_y = vel[1]

        if DIMENSIONS > 2:
            z = coord[2]
            vel_z = vel[2]

            if not(MIN_Z < z < MAX_Z):
                if vel_z * z < 0:
                    return True

        if not(MIN_Y < x < MAX_Y):
            if vel_x * x < 0:
                return True

        if not(MIN_X < x < MAX_X):
            if vel_x * x < 0:
                return True


    
    def get_coords(self):
        return self.coords

    def get_velocity(self):
        return self.velocity

    def get_radius(self):
        return self.radius
