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

    def __init__(self, x, y, image, logical):
        # String of the path of the image
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.logical = logical

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_xy(self):
        return self.x, self.y

    def allowed_moves(self):
        raise NotImplementedError

    def __eq__(self, string):
        return True if string == self.logical else False


class PRook(Piece):
    def allowed_moves(self):
        raise NotImplementedError


class PKnight(Piece):
    def allowed_moves(self):
        raise NotImplementedError


class PBishop(Piece):
    def allowed_moves(self):
        raise NotImplementedError


class PQueen(Piece):
    def allowed_moves(self):
        raise NotImplementedError


class PKing(Piece):
    def allowed_moves(self):
        raise NotImplementedError


class PPawn(Piece):
    def allowed_moves(self):
        raise NotImplementedError


whiteRook = PRook(
    x=None, y=None, image=symbolsPath[current_theme]["white_rook"], logical="wr"
)
blackRook = PRook(
    x=None, y=None, image=symbolsPath[current_theme]["black_rook"], logical="br"
)
whiteKnight = PKnight(
    x=None, y=None, image=symbolsPath[current_theme]["white_knight"], logical="wn"
)
blackKnight = PKnight(
    x=None, y=None, image=symbolsPath[current_theme]["black_knight"], logical="bn"
)
whiteBishop = PBishop(
    x=None, y=None, image=symbolsPath[current_theme]["white_bishop"], logical="wb"
)
blackBishop = PBishop(
    x=None, y=None, image=symbolsPath[current_theme]["black_bishop"], logical="bb"
)
whiteQueen = PQueen(
    x=None, y=None, image=symbolsPath[current_theme]["white_queen"], logical="wq"
)
blackQueen = PQueen(
    x=None, y=None, image=symbolsPath[current_theme]["black_queen"], logical="bq"
)
whiteKing = PKing(
    x=None, y=None, image=symbolsPath[current_theme]["white_king"], logical="wk"
)
blackKing = PKing(
    x=None, y=None, image=symbolsPath[current_theme]["black_king"], logical="bk"
)
whitePawn = PPawn(
    x=None, y=None, image=symbolsPath[current_theme]["white_pawn"], logical="wp"
)
blackPawn = PPawn(
    x=None, y=None, image=symbolsPath[current_theme]["black_pawn"], logical="bp"
)

chessSet = (
    whiteRook,
    blackRook,
    whiteKnight,
    blackKnight,
    whiteBishop,
    blackBishop,
    whiteQueen,
    blackQueen,
    whiteKnight,
    blackKing,
    whitePawn,
    blackPawn,
)
