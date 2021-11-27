#!/usr/bin/python3

## Standard Library imports
import os
import pygame

## Local imports
import board
from board import Pos

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
        self.fps = fps
        self.running = True
        self.change = False  # To signal if there is something to render and update from user input
        self.selected = False  # if a square has been picked by the user
        self.pos = Pos(7, 4)  # where the selected square is, by default where king is
        self.board = board.Board(pos=self.pos)
        # Start drawing the initial board
        # Should be probably moved to render, so that the board is not drawn when the object is instantiated
        self.board.board_setup()

    def process_input(self):
        # for now only keyboard
        # 4 directions, enter and esc
        # TODO: mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.change = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.selected = False
                    self.change = True
                    break
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.selected = False if self.selected == True else True
                    self.change = True
                    break
                elif event.key == pygame.K_RIGHT:
                    self.pos.y += 1 if self.pos.x < 7 else 7
                    self.change = True
                    break
                elif event.key == pygame.K_LEFT:
                    self.pos.y -= 1 if self.pos.y != 0 else 0
                    self.change = True
                    break
                elif event.key == pygame.K_DOWN:
                    self.pos.x += 1 if self.pos.x < 7 else 7
                    self.change = True
                    break
                elif event.key == pygame.K_UP:
                    self.pos.x -= 1 if self.pos.x != 0 else 0
                    self.change = True
                    break

    def update(self):
        # Todo: check if it is ok to simply eq two objects, maybe it is better so use a setter method in the board obj

        self.board.pos.x = self.pos.x
        self.board.pos.y = self.pos.y

    def render(self):
        print(self.board.pos.x, self.board.pos.y, self.pos.x, self.pos.y)
        self.board.board_setup()

    def run(self):
        while self.running == True:
            self.process_input()
            if self.change:
                self.update()
                self.render()
                self.change = False
            self.clock.tick(self.fps)
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
