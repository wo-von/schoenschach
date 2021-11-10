#!/usr/bin/python3

# external libraries
import pygame
import sys
import os
import time

# local libraries
from pieces import *


class Board(object):
    """
    Logical representation of a board
    """

    def __init__(self):
        self.board = [
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
        ]

    def update(self):
        return self.board


def main():

    BLACK = (0, 0, 0)
    GRAY = (180, 180, 180)
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
    time.sleep(10)
    # Draw the pieces
    # bishopBlack = Piece(250, 50, "../assets/pieces/2048px-BishopB.svg.png")
    blackBishop.image = pygame.transform.scale(blackBishop.image, (100, 100))
    blackBishop.x = 250
    blackBishop.y = 50
    screen.blit(blackBishop.image, (blackBishop.x, blackBishop.y))
    pygame.display.flip()
    x_dest = 450
    y_dest = 250
    step = 20
    while blackBishop.x < x_dest and blackBishop.y < y_dest:
        time.sleep(0.05)
        blackBishop.x += step
        blackBishop.y += step
        screen.blit(board, (padding, padding))
        screen.blit(blackBishop.image, (blackBishop.x, blackBishop.y))
        pygame.display.flip()
    while True:
        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit() alone does not work
                pygame.display.quit()


if __name__ == "__main__":
    main()
