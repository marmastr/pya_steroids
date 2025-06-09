import pygame
import constants


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    _, _ = pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    ticker = pygame.time.Clock()
    dt = 0
    i = 0
    while i < 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = screen.fill("black")
        pygame.display.flip()
        dt = ticker.tick(60)/1000


if __name__ == "__main__":
    main()
