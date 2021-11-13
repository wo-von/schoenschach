#!/usr/bin/python3

# external libraries
import pygame
import sys
import os
import time

# local libraries
import pieces

gameTypes = {"standard"}

standardBoard = [
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
]


class Board(object):
    """
    Logical representation of a board
    """

    def __init__(
        self, screenSize=(900, 900), padding=50, logicalsize=(8, 8), gameType="standard"
    ):
        self.screenSize = self.height, self.width = screenSize
        self.logicalsize = self.logical_height, self.logical_width = logicalsize
        self.padding = padding
        self.logical_board = standardBoard if gameType == "standard" else None
        self.board = self.get_board()
    def update(self):
        return self.board

    def get_coordinates(self):
        return [
            (x, y)
            for y in range(
                self.padding,
                self.height - self.padding,
                int((self.height - 2 * self.padding) / self.logical_height),
            )
            for x in range(
                self.padding,
                self.width - self.padding,
                int((self.width - 2 * self.padding) / self.logical_width),
            )
        ]
    def get_board(self):
        '''
        builds up a board with piece objects from pieces.py based on the logical_board
        '''
        

def main():

    BLACK = (0, 0, 0)
    GRAY = (180, 180, 180)
    board_logical_size = logical_height, logical_width = 8, 8
    screenSize = height, width = 900, 900
    padding = 50
    # Start all modules
    pygame.init()
    # Call the screen Schönschach
    pygame.display.set_caption("Schönschach")  # make icon also working
    # Draw s 1000 * 1000 screen
    screen = pygame.display.set_mode(screenSize)
    board = pygame.image.load("../assets/boards/Chessboard480.svg.png")

    # Load the board image and transform its scale with the corresponding padding
    # now: 800 * 800 for simplicity
    board = pygame.transform.scale(board, (height - 2 * padding, width - 2 * padding))
    screen.fill(GRAY)
    screen.blit(board, (padding, padding))

    # Draw the pieces

    test_bishop = pieces.BBishop(250, 50)
    test_bishop.image = pygame.transform.scale(test_bishop.image, (100, 100))
    screen.blit(test_bishop.image, test_bishop.get_xy())
    pygame.display.flip()
    # x_dest = 450
    # y_dest = 250
    # step = 20
    # while blackBishop.x < x_dest and blackBishop.y < y_dest:
    #     time.sleep(0.05)
    #     blackBishop.x += step
    #     blackBishop.y += step
    #     screen.blit(board, (padding, padding))
    #     screen.blit(blackBishop.image, (blackBishop.x, blackBishop.y))
    #     pygame.display.flip()
    while True:
        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit() alone does not work
                pygame.display.quit()


if __name__ == "__main__":
    main()
