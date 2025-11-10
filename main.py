import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
import os

def main():
    pygame.init()
    pygame.font.init()

    name = input("Enter your name for the scoreboard: ")
    screen = pygame.display.set_mode((1366, 768))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    with open("./high_score.txt", 'r') as f:
        high_score = f.read()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set groups for Player class and create Player instance
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set groups for Asteroid class and create Asteroid instance
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set AsteroidField containers
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    # Set Shot class containers
    Shot.containers = (shots, updatable, drawable)
    

    print("Starting Asteroids!")
    print(f"Screen width: 1366")
    print(f"Screen height: 768")



    while True:
        log_state()
        font = pygame.font.Font(None, 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        # Check for asteroid collision with player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                with open("./high_score.txt", 'r') as f:
                    content = f.read()
                    if int(content.split(':')[1]) < score:
                        with open("./high_score.txt", 'w') as f:
                            f.write(f"{name}: {score}")
                    print(f"Your score: {score}")
                print("High Score:")
                print(content)
                    
                sys.exit()

        # Check for asteroid collision with player shot
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    score += 10

        # Draw score to screen
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Draw high score to screen
        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_text, (1000, 10))

        pygame.display.flip()


if __name__ == "__main__":
    main()

