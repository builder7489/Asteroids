import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position , self.radius, 2)
    
    def update(self, dt):
        self.position +=(self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # spawn new asteroids
        else:
            random_angle = random.uniform(20, 50)

            velocity_new = self.velocity.rotate(random_angle)
            velocity_newb = self.velocity.rotate(-(random_angle))

            radius_new = self.radius - ASTEROID_MIN_RADIUS

            asteroid_new = Asteroid(self.position.x, self.position.y, radius_new)
            asteroid_new.velocity = velocity_new * 1.2
            asteroid_newb = Asteroid(self.position.x, self.position.y, radius_new)
            asteroid_newb.velocity = velocity_newb * 1.2



