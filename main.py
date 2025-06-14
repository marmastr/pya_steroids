import sys
import pygame
from asteroid import Asteroid
import asteroidfield
import constants
from player import Player
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    _, _ = pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    ticker = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)

    field_of_rocks = AsteroidField()
    player = Player(x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2)

    i = 0
    while i < 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for rock in asteroids:
            for bullet in shots:
                if rock.collision(bullet):
                    rock.kill()
                    bullet.kill()
            if rock.collision(player):
                print("Game over!")
                sys.exit(0)

        _ = screen.fill("black")

        for object in drawable:
            object.draw(screen=screen)

        pygame.display.flip()

        dt = ticker.tick(60) / 1000


if __name__ == "__main__":
    main()
