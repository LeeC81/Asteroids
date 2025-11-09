import pygame
from constants import *
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set groups for Player class and create Player instance
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        pygame.display.flip()


if __name__ == "__main__":
    main()

