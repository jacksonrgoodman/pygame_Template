import pygame
import sys
from settings import *
from debug import debug


class Game:
    def __init__(self):
        # ? Game Setup
        pygame.init()
        pygame.display.set_icon(pygame.image.load("a.png"))
        pygame.display.set_caption("PROGRAM")
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("EXITING_GAME")
                    sys.exit()

            self.screen.fill('black')
            debug("GAME_RUNNING")
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
