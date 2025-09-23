
# using the open source pygame library
import pygame
import sys

# using magic numbers in the game
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups for the game loop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adding groups to objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Add player with center starting point
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # game background
        screen.fill("black")

        dt = game_clock.tick(60) / 1000

        # update all updatable items
        #for item in updatable:
        updatable.update(dt)

        # draw/ render all items individually
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()
