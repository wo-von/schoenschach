#!/usr/bin/python3

class PieceGeneral(object):
    pass

class Piece(PieceGeneral):
    '''
    Normal piece on a 2d board
    has x, y as column and row
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pawn(Piece):
    def __init__(self, x, y):
        Piece.__init__(self, x, y)
class Rook(Piece):
    def __init__(self, x, y):
        Piece.__init__(self, x, y)
class Bishop(Piece):
    def __init__(self, x, y):
        Piece.__init__(self, x, y)
class Knight(Piece):
    def __init__(self, x, y):
        Piece.__init__(self, x, y)
class Queen(Piece):
    def __init__(self, x, y):
        Piece.__init__(self, x, y)
class King(Piece):
    def __init__(self, x, y):
        Piece.__init__(self, x, y)