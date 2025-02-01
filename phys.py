import particle
from particle import Particle
import random

DIMENSIONS = particle.DIMENSIONS
BODIES = 11
DT = 1e-5
G = 6.67e-11


MIN_MASS = 1e21
MAX_MASS = 1e23
MIN_X = -500
MIN_Y = -500
MAX_X = 500
MAX_Y = 500

SPAWN_CONST = 0.5

class Physics:
    def __init__(self):
        """Initializes a Physics object and several Particle objects with mass"""

        self.particles = []
        initCoordsAllParticles = []


        # initialize all particles
        while len(initCoordsAllParticles) < BODIES:
            x = SPAWN_CONST * random.uniform(MIN_X, MAX_X)
            y = SPAWN_CONST * random.uniform(MIN_Y, MAX_Y)

            coords = [x, y]
            if coords in initCoordsAllParticles:
                continue

            mass = random.uniform(MIN_MASS, MAX_MASS)
            initCoordsAllParticles.append(coords)

            self.particles.append(Particle(mass, coords))


    def update_accel(self):
        """Updates all particle's acceleration based on F = Gmmr/|r|^3"""

        for p1 in self.particles:
            new_accel = []

            for p2 in self.particles:
                if p1 is p2:
                    continue
                dist_vector = [p1.coords[dim] - p2.coords[dim] for dim in range(DIMENSIONS)]
                r_squared = [d ** 2 for d in dist_vector]
                r = sum(r_squared) ** 0.5

                for dim in range(DIMENSIONS):
                    a_dim = -G * p2.mass * dist_vector[dim] / (r ** 3)
                    new_accel.append(a_dim)

            p1.set_accel(new_accel)




    def update_velocity(self):
        """Updates all particle's velocities based on acceleration and current velocity"""

        for particle in self.particles:
            particle.update_velocity(DT)

    def update_coords(self):
        """Updates all particle's coordinates based on accel and vel"""

        for particle in self.particles:
            particle.update_coords(DT)

    def get_coords(self):
        out = []

        for particle in self.particles:
            coord = list(particle.coords)
            out.append(coord)

        return out

    def get_velocities(self):
        out = []

        for particle in self.particles:
            vel = list(particle.velocity)
            out.append(vel)
        return out

    def get_accels(self):
        out = []
        
        for particle in self.particles:
            accel = list(particle.accel)
            out.append(accel)

        return out



    def print_coords(self):
        for particle in self.particles:
            print(particle.coords)
