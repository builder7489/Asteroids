# using the open source pygame library
import pygame

# using magic numbers in the game
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # player starting location
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)   

    # Start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # game background
        screen.fill("black")
        
        # render player
        # print(type(player.draw(screen)))
        # print(player.triangle())
        # print(x, y)

        player.draw(screen)

        pygame.display.flip()

        game_clock.tick(60)
        dt = game_clock.tick() / 1000



if __name__ == "__main__":
    main()
