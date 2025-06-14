from curses import KEY_UP
import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: int = 0
        self.timer: float = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        _ = pygame.draw.polygon(
            surface=screen, color="white", points=self.triangle(), width=2
        )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] | keys[pygame.K_LEFT]:
            self.rotate(0 - dt)
        if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] | keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] | keys[pygame.K_DOWN]:
            self.move(0 - dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            # if self.timer > 0:
            self.timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        )
        self.timer = PLAYER_SHOOT_COOLDOWN
