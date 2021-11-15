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
    """

    def __init__(
        self, screenSize=(900, 900), padding=50, logicalsize=(8, 8), gameType="standard"
    ):
        self.screenSize = self.height, self.width = screenSize
        self.logicalsize = self.logical_height, self.logical_width = logicalsize
        self.padding = padding
        self.logical_board = standardBoard if gameType == "standard" else None
        self.board = self.get_board()

    def update(self):
        return self.board

    def get_coordinates(self):
        
        self.coordinates = list()
        for y in range(
                self.padding,
                self.height - self.padding,
                int((self.height - 2 * self.padding) / self.logical_height),
            ):
            row = list()
            for x in range(
                self.padding,
                self.width - self.padding,
                int((self.width - 2 * self.padding) / self.logical_width),
            ):
                row.append((x, y))
            self.coordinates.append(row)
        return self.coordinates

    def get_board(self):
        """
        builds up a board with piece objects from pieces.py based on the logical_board
        """
        temp = list()  # empty list with correct rows and columns to be filled
        for _ in range(self.logical_height):
            temptemp = list()
            for _ in range(self.logical_width):
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


def main():

    BLACK = (0, 0, 0)
    GRAY = (180, 180, 180)
    board_logical_size = logical_height, logical_width = 8, 8
    screenSize = height, width = 900, 900
    padding = 50
    # Start all modules
    pygame.init()
    # Call the screen Schönschach
    pygame.display.set_caption("Schönschach")  # make icon also working
    # Draw a 900 * 900 screen
    screen = pygame.display.set_mode(screenSize)
    board = pygame.image.load("../assets/boards/Chessboard480.svg.png")

    # Load the board image and transform its scale with the corresponding padding
    # now: 800 * 800 for simplicity
    board = pygame.transform.scale(board, (height - 2 * padding, width - 2 * padding))
    screen.fill(GRAY)
    screen.blit(board, (padding, padding))
    pygame.display.flip()
    # Draw the pieces
    logical_size = rows, columns = 8, 8
    game = Board(logicalsize=logical_size)
    toDraw = game.get_board()
    co = game.get_coordinates()
    for i in range(rows):
        for j in range(columns):
            thisPiece = toDraw[i][j].piece
            if thisPiece == None:
                continue
            thisPiece.image = pygame.transform.scale(thisPiece.image, (100, 100))

            screen.blit(thisPiece.image, co[i][j])

    pygame.display.flip()
    
    while True:
        time.sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit() alone does not work
                pygame.display.quit()


if __name__ == "__main__":
    main()
