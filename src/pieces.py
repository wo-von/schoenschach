#!/usr/bin/python3

import pygame

Themes = ["normal"]
current_theme = Themes[0]

# ToDo: use os.path.join or sth nicer here
symbolsPath = {
    "normal": {
        "wr": "../assets/pieces/2048px-RookW.svg.png",
        "br": "../assets/pieces/2048px-RookB.svg.png",
        "wn": "../assets/pieces/2048px-KnightW.svg.png",
        "bn": "../assets/pieces/2048px-KnightB.svg.png",
        "wb": "../assets/pieces/2048px-BishopW.svg.png",
        "bb": "../assets/pieces/2048px-BishopB.svg.png",
        "wq": "../assets/pieces/2048px-QueenW.svg.png",
        "bq": "../assets/pieces/2048px-QueenB.svg.png",
        "wk": "../assets/pieces/2048px-KingW.svg.png",
        "bk": "../assets/pieces/2048px-KingB.svg.png",
        "wp": "../assets/pieces/2048px-PawnW.svg.png",
        "bp": "../assets/pieces/2048px-PawnB.svg.png",
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


class Rook(Piece):
    @property
    def allowed_moves(self):
        temp = list()
        for i in range(1, 8):
            if self.x + i <= 7:
                temp.append([self.x + i, self.y])
            if self.x - i >= 0:
                temp.append([self.x - i, self.y])
        for i in range(1, 8):
            if self.y + i <= 7:
                temp.append([self.x, self.y + i])
            if self.y - i >= 0:
                temp.append([self.x, self.y - i])
        return temp


class WRook(Rook):
    logical, color = "wr", "w"

    def __init__(self, x, y):
        Rook.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=WRook.logical,
        )


class BRook(Rook):
    logical, color = "br", "b"

    def __init__(self, x, y):
        Rook.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=BRook.logical,
        )


class Knight(Piece):
    @property
    def allowed_moves(self):
        temp = list()
        # ToDo: maybe use permutations from itertools here
        for i, j in zip([-2, -1, 1, 2], [1, 2, 2, 1]):
            if self.x + i >= 0 and self.x + i <= 7:
                if self.y + j <= 7:
                    temp.append([self.x + i, self.y + j])
                if self.y - j >= 0:
                    temp.append([self.x + i, self.y - j])
        return temp


class WKnight(Knight):
    logical, color = "wn", "w"

    def __init__(self, x, y):
        Knight.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=WKnight.logical,
        )


class BKnight(Knight):
    logical, color = "bn", "b"

    def __init__(self, x, y):
        Knight.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=BKnight.logical,
        )


class Bishop(Piece):
    @property
    def allowed_moves(self):
        temp = list()
        for i in range(1, 8):
            temp.append(
                [self.x + i, self.y + i]
            ) if self.x + i <= 7 and self.y + i <= 7 else None
            temp.append(
                [self.x - i, self.y - i]
            ) if self.x - i >= 0 and self.y - i >= 0 else None
            temp.append(
                [self.x + i, self.y - i]
            ) if self.x + i <= 7 and self.y - i >= 0 else None
            temp.append(
                [self.x - i, self.y + i]
            ) if self.x - i >= 0 and self.y + i <= 7 else None
        return temp


class WBishop(Bishop):
    logical, color = "wb", "w"

    def __init__(self, x, y):
        Bishop.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=WBishop.logical,
        )


class BBishop(Bishop):
    logical, color = "bb", "b"

    def __init__(self, x, y):
        Bishop.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=BBishop.logical,
        )


class Queen(Piece):
    def allowed_moves(self):
        raise NotImplementedError


class WQueen(Queen):
    logical, color = "wq", "w"

    def __init__(self, x, y):
        Queen.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=WQueen.logical,
        )


class BQueen(Queen):
    logical, color = "bq", "b"

    def __init__(self, x, y):
        Queen.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=BQueen.logical,
        )


class King(Piece):
    def allowed_moves(self):
        raise NotImplementedError

    def is_checked(self):
        raise NotImplementedError

    def is_mate(self):
        raise NotImplementedError


class WKing(King):
    logical, color = "wk", "w"

    def __init__(self, x, y):
        King.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=WKing.logical,
        )


class BKing(King):
    logical, color = "bk", "b"

    def __init__(self, x, y):
        King.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=BKing.logical,
        )


class Pawn(Piece):
    def allowed_moves(self):
        raise NotImplementedError


class WPawn(Pawn):
    logical, color = "wp", "w"

    def __init__(self, x, y):
        Pawn.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=WPawn.logical,
        )


class BPawn(Pawn):
    logical, color = "bp", "b"

    def __init__(self, x, y):
        Pawn.__init__(
            self,
            x=x,
            y=y,
            image=symbolsPath[current_theme][self.logical],
            logical=BPawn.logical,
        )
