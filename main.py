# using the open source pygame library
import pygame

# using magic numbers in the game
from constants import *
from player import Player

def main():
    pygame.init

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # player starting location
    x_location = SCREEN_WIDTH / 2
    y_location = SCREEN_HEIGHT / 2

    player = Player(x_location, y_location, PLAYER_RADIUS)   

    # Start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        # render player
        player.draw(screen)

        pygame.display.flip

        game_clock.tick(60)
        dt = game_clock.tick(60) / 1000



if __name__ == "__main__":
    main()
