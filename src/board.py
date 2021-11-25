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
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
]


class Square(object):
    """
    What each square entails: i, j,  (coordinates), standard coordinate (a-h and 1-8 for standard voard), and piece
    Null for empty squares
    """

    def __init__(self, i, j, piece):
        self.i = i
        self.j = j
        self.piece = piece


class Board(object):
    """
    Logical representation of a board
    empty_board: string of the path to the empty board file
    board: pygame loaded image of the empty_board
    """

    def __init__(
        self,
        screenSize=(900, 900),
        padding=50,
        logicalsize=(8, 8),
        gameType="standard",
        empty_board="../assets/boards/Chessboard480.svg.png",
        caption="Schönschach",
        pos=[1, 5],
    ):
        self.screenSize = self.height, self.width = screenSize
        self.logicalsize = self.rows, self.columns = logicalsize
        self.padding = padding
        self.logical_board = standardBoard if gameType == "standard" else None
        self.empty_board = empty_board
        self.caption = caption
        self.emptyboard = pygame.image.load(
            self.empty_board
        )  # Picture of the empty board
        self.pos = pos  # Where the user is pointing
        self.board = self.get_board()  # collection of all the piece objects
        # This takes a very long time, TODO: optimize!

    def draw_pieces(self):
        """
        draw the board
        """
        co = self.get_coordinates()
        for i in range(self.rows):
            for j in range(self.columns):
                thisPiece = self.board[i][j].piece
                if thisPiece == None:
                    continue
                thisPiece.image = pygame.transform.scale(thisPiece.image, (100, 100))

                self.display.blit(thisPiece.image, co[i][j])
        pygame.display.flip()  # This bothers me, how can I do it specific to this class?

    def get_coordinates(self):
        """
        Where each piece should be drawn, based on the screenSize (top left corner of each square)
        """
        self.coordinates = list()
        for y in range(
            self.padding,
            self.height - self.padding,
            int((self.height - 2 * self.padding) / self.rows),
        ):
            row = list()
            for x in range(
                self.padding,
                self.width - self.padding,
                int((self.width - 2 * self.padding) / self.columns),
            ):
                row.append((x, y))
            self.coordinates.append(row)
        return self.coordinates

    def get_dimensions(self):
        """
        calculates and updates the dimensions needed
        screenSize and padding are for now fixed
        """
        self.cell_size = int((self.width - 2 * self.padding) / self.columns)
        return self.cell_size

    def get_board(self):
        """
        builds up a board with piece objects from pieces.py based on the logical_board
        """
        temp = list()  # empty list with correct rows and columns to be filled
        for _ in range(self.columns):
            temptemp = list()
            for _ in range(self.rows):
                temptemp.append([])
            temp.append(temptemp)

        for n, row in enumerate(self.logical_board):
            for m, column in enumerate(row):
                if self.logical_board[n][m] == "wp":
                    temp[n][m] = Square(m, n, pieces.WPawn(m, n))

                elif self.logical_board[n][m] == "wr":
                    temp[n][m] = Square(m, n, pieces.WRook(m, n))

                elif self.logical_board[n][m] == "wn":
                    temp[n][m] = Square(m, n, pieces.WKnight(m, n))

                elif self.logical_board[n][m] == "wb":
                    temp[n][m] = Square(m, n, pieces.WBishop(m, n))

                elif self.logical_board[n][m] == "wq":
                    temp[n][m] = Square(m, n, pieces.WQueen(m, n))

                elif self.logical_board[n][m] == "wk":
                    temp[n][m] = Square(m, n, pieces.WKing(m, n))

                elif self.logical_board[n][m] == "bp":
                    temp[n][m] = Square(m, n, pieces.BPawn(m, n))

                elif self.logical_board[n][m] == "br":
                    temp[n][m] = Square(m, n, pieces.BRook(m, n))

                elif self.logical_board[n][m] == "bn":
                    temp[n][m] = Square(m, n, pieces.BKnight(m, n))

                elif self.logical_board[n][m] == "bb":
                    temp[n][m] = Square(m, n, pieces.BBishop(m, n))

                elif self.logical_board[n][m] == "bq":
                    temp[n][m] = Square(m, n, pieces.BQueen(m, n))

                elif self.logical_board[n][m] == "bk":
                    temp[n][m] = Square(m, n, pieces.BKing(m, n))
                elif self.logical_board[n][m] == 0:
                    temp[n][m] = Square(m, n, None)
                else:
                    raise ValueError(
                        "self.logical_board[m][n] does not have a valid piece:",
                        self.logical_board[n][m],
                        n,
                        m,
                    )
        return temp

    def draw_empty_board(self):
        """
        draws and empty board, over which the game is played
        """
        # TODO: add icon for the display
        self.display = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption(self.caption)
        self.emptyboard = pygame.transform.scale(
            self.emptyboard,
            (self.height - 2 * self.padding, self.width - 2 * self.padding),
        )
        self.display.fill((180, 180, 180))  # GRAY
        self.display.blit(self.emptyboard, (self.padding, self.padding))
        pygame.display.flip()

    def draw_square(self):
        """
        draws a square for the user to pick pieces
        """
        pygame.draw.rect(self.display, (255, 255, 0), (10, 10, 100, 100), 3)
        pygame.display.flip()
