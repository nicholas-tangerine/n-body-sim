import constants

DIMENSIONS = constants.DIMENSIONS

class Particle:
    def __init__(self, mass, coords, v = None, a = None):
        """Initializes a Particle object with mass and coordinates"""

        self.mass = mass
        self.coords = coords

        if not v:
            v = [0] * DIMENSIONS
        if not a:
            a = [0] * DIMENSIONS

        self.velocity = v
        self.accel = a
    
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
