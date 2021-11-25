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
    1) Initialize game state
    2) process input
    3) update game state
    4) render changes
    """

    def __init__(self, fps=60):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.board = board.Board()
        self.fps = fps
        self.running = True
        self.selected = False  # if a square has been picked by the user
        self.pos = [1, 5]  # where the selected square is, by default where king is
        # Start drawing the initial board
        # Should be probably moved to render, so that the board is not drawn when the object is instantiated
        self.board.draw_empty_board()
        self.board.draw_pieces()

    def process_input(self):
        # for now only keyboard
        # 4 directions, enter and esc
        # TODO: mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.selected = False
                elif event.key == pygame.K_SPACE or event.key == pygame.KEY_RETURN:
                    self.selected = False if self.selected == True else True
                elif event.key == pygame.K_RIGHT:
                    self.pos[1] += 1 if self.pos[1] < 7 else 7
                elif event.key == pygame.K_LEFT:
                    self.pos[1] -= 1 if self.pos[1] != 0 else 0
                elif event.key == pygame.K_DOWN:
                    self.pos[0] += 1 if self.pos[0] < 7 else 7
                elif event.key == pygame.K_UP:
                    self.pos[0] -= 1 if self.pos[0] != 0 else 0

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
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
