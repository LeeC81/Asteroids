import pygame
from constants import *
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,  LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

        # Screen wrap asteroids
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            self.split_velocity = self.velocity.rotate(angle)
            self.split_velocity2 = self.velocity.rotate(-angle)
            self.split_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, self.split_radius)
            asteroid1.velocity = self.split_velocity * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, self.split_radius)
            asteroid2.velocity = self.split_velocity2 * 1.2



