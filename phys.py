import constants

import particle
from particle import Particle

import random

import time

DIMENSIONS = constants.DIMENSIONS
BODIES = constants.BODIES
DT = constants.DT
G = constants.G


MIN_MASS = constants.MIN_MASS
MAX_MASS = constants.MAX_MASS

MIN_X = constants.MIN_X
MAX_X = constants.MAX_X

MIN_Y = constants.MIN_Y
MAX_Y = constants.MAX_Y

MIN_Z = constants.MIN_Z
MAX_Z = constants.MAX_Z

INITIAL_POSITION_FACTOR = constants.INITIAL_POSITION_FACTOR

class Physics:
    def __init__(self):
        """Initializes a Physics object and several Particle objects with mass"""

        self.particles = []
        initCoordsAllParticles = []

        # initialize all particles
        while len(initCoordsAllParticles) < BODIES:
            x = INITIAL_POSITION_FACTOR * random.uniform(MIN_X, MAX_X)
            y = INITIAL_POSITION_FACTOR * random.uniform(MIN_Y, MAX_Y)
            
            coords = [x, y]

            if DIMENSIONS > 2:
                z = INITIAL_POSITION_FACTOR * random.uniform(MIN_Z, MAX_Z)
                coords.append(z)

            if coords in initCoordsAllParticles:
                continue

            mass = random.uniform(MIN_MASS, MAX_MASS)
            initCoordsAllParticles.append(coords)

            self.particles.append(Particle(mass, coords))


    def update_accel(self):
        """
        Updates all particle's acceleration based on F = Gmmr/|r|^3
        Also checks to make sure particles are on screen. if not, deleted from mem
        """

        for p1 in self.particles:
            new_accel = [0] * DIMENSIONS

            for p2 in self.particles:
                if p1 is p2:
                    continue
                dist_vector = [p1.coords[dim] - p2.coords[dim] for dim in range(DIMENSIONS)]
                r_squared = [d ** 2 for d in dist_vector]
                r = sum(r_squared) ** 0.5

                for dim in range(DIMENSIONS):
                    new_accel[dim] += -G * p2.mass * dist_vector[dim] / (r ** 3)

            p1.set_accel(new_accel)
        
        for i in range(len(self.particles)-1, -1, -1):
            particle = self.particles[i]

            if particle.gone_forever():
                del self.particles[i]

    def update_velocity(self):
        """Updates all particle's velocities based on acceleration and current velocity"""

        for particle in self.particles:
            particle.update_velocity(DT)

    def update_coords(self):
        """Updates all particle's coordinates based on accel and vel"""

        for particle in self.particles:
            particle.update_coords(DT)


    def get_particles(self):
        out = []
        
        for particle in self.particles:
            out.append(particle)

        return out

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
