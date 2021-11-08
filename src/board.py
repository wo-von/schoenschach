#!/usr/bin/python3

# external libraries
import pygame
import sys
import os
# local libraries
from pieces import Piece

class Board(object):
    '''
    Logical representation of a board
    '''
    def __init__(self):
        self.board = [["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"], ["wp", "wp","wp","wp","wp","wp","wp","wp"], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"], ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"]]
    def update(self):
        return self.board

def main():
    
    BLACK = (0, 0, 0)
    GRAY = (180, 180, 180)
    screenSize = height, width = 800, 800
    padding = 30
    # Start all modules
    pygame.init()
    
    pygame.display.set_caption("Schönschach") # make icon also working
    
    screen = pygame.display.set_mode(screenSize)
    # simple_board.png is 1000*1000
    board = pygame.image.load("../assets/boards/Chessboard480.svg.png")
    
    # resize the board to fit to the screen
    board = pygame.transform.scale(board, (height, width))
    
    screen.fill(GRAY)
    screen.blit(board, (padding, padding))
    # Update the display
    
    # Draw the pieces
    bishop = Piece(250, 50, "../assets/pieces/Chess_bdt60.png")
    bishop.image = pygame.transform.scale(bishop.image, (80, 80))
    screen.blit(bishop.image, (bishop.x, bishop.y))
    pygame.display.flip()
    
    while True:
        import time
        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit() alone does not work
                pygame.display.quit()

if __name__ == '__main__':
    main()

