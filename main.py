import argparse
import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroidfield import AsteroidField
from shot import Shot
from scored import scorer

parser = argparse.ArgumentParser()
parser.add_argument(
    "-n",
    "--name",
    dest="name",
    default="Anonymous",
    help="file in directory you wish to import",
    type=str,
)
args = parser.parse_args()


def main():
    score: int = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    _, _ = pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    i = 0
    while i < 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for rock in asteroids:
            for bullet in shots:
                if rock.collision(bullet):
                    rock.split()
                    bullet.kill()
                    score += 1
            if rock.collision(player):
                scorer(score, args.name)

        _ = screen.fill("black")

        for object in drawable:
            object.draw(screen=screen)

        pygame.display.flip()

        dt = ticker.tick(60) / 1000


if __name__ == "__main__":
    main()
