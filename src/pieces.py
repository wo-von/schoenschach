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
        # String of the path of the image
        self.image = pygame.image.load(image) 
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x = x
        self.y = y
    def get_xy(self):
        return self.x, self.y
