#!/usr/bin/python3
import pygame
class PieceGeneral(object):
    pass

class Piece(PieceGeneral):
    '''
    Normal piece on a 2d board
    has x, y as column and row
    '''
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        # String of the path of the image
        self.image = pygame.image.load(image) 
    def move(self, x, y):
        self.x = x
        self.y = y