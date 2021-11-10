#!/usr/bin/python3
import pygame
from enum import Enum


Themes = ["normal"]
current_theme = Themes[0]

symbolsPath = {
    "normal": {
        "white_pawn": "../assets/pieces/2048px-PawnW.svg.png",
        "black_pawn": "../assets/pieces/2048px-PawnB.svg.png",
        "white_knight": "../assets/pieces/2048px-KnightW.svg.png",
        "black_knight": "../assets/pieces/2048px-KNightB.svg.png",
        "white_bishop": "../assets/pieces/2048px-BishopW.svg.png",
        "black_bishop": "../assets/pieces/2048px-BishopB.svg.png",
        "white_rook": "../assets/pieces/2048px-RookW.svg.png",
        "black_rook": "../assets/pieces/2048px-RookB.svg.png",
        "white_queen": "../assets/pieces/2048px-QueenW.svg.png",
        "black_queen": "../assets/pieces/2048px-QueenB.svg.png",
        "black_king": "../assets/pieces/2048px-KingB.svg.png",
        "black_king": "../assets/pieces/2048px-KingW.svg.png",
    }
}


class Piece(object):
    """
    Normal piece on a 2d board
    has x, y as column and row
    """

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

    def allowed_moves(self):
        raise NotImplementedError


class PBishop(Piece):
    def allowed_moves(self):
        raise NotImplementedError


whiteBishop = PBishop(x=None, y=None, image=symbolsPath[current_theme]["white_bishop"])
blackBishop = PBishop(x=None, y=None, image=symbolsPath[current_theme]["black_bishop"])
