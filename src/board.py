#!/usr/bin/python3

import pygame
import sys
import os

def main():
    
    BLACK = (0, 0, 0)
    GRAY = (180, 180, 180)
    screenSize = height, width = 800, 800
    padding = 30
    # Start all modules
    pygame.init()
    
    pygame.display.set_caption("Schönschach") # make icon also working
    
    screen = pygame.display.set_mode(screenSize)
    piece = pygame.image.load("../assets/pieces/Chess_bdt60.png")
    # simple_board.png is 1000*1000
    board = pygame.image.load("../assets/boards/simple_board.png")
    
    # resize the board to fit to the screen
    board = pygame.transform.scale(board, (height - 2 * padding, width - 2* padding))
    
    screen.fill(GRAY)
    screen.blit(board, (padding, padding))
    # Update the display
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit() alone does not work
                pygame.display.quit()
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()

