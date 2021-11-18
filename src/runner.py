## Standard Library imports
import os
import pygame

## Local imports
import board
import pieces

os.environ["SDL_VIDEO_CENTERED"] = "1"


class Game(object):
    """
    Main game class based on the game-dev run:
    seperate app into
    1) process input
    2) update game state
    3) render changes
    """

    def __init__(self, fps=60):
        pygame.init()
        self.clock = pygame.time.clock()
        self.board = board.Board()
        self.fps = fps

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def run(self):
        while self.running == True:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
