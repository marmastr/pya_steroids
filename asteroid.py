import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="gray",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle: float = random.uniform(20, 50)
        new_vec1 = self.velocity.rotate(angle)
        new_vec2 = -new_vec1
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        rock1 = Asteroid(self.position.x, self.position.y, new_radius)
        rock2 = Asteroid(self.position.x, self.position.y, new_radius)
        rock1.velocity = new_vec1 * 1.2
        rock2.velocity = new_vec2
