import numpy as np


class pyGammon:

    def __init__(self):
        self.board = np.zeros(24, dtype="i1")
        self.jail = np.zeros(2, dtype="i1")
        self.rolled_off = np.zeros(2, dtype="i1")

        self.board[0] = -2
        self.board[5] = 5
        self.board[7] = 3
        self.board[11] = -5
        self.board[12] = 5
        self.board[16] = -3
        self.board[18] = -5
        self.board[23] = 2

    def __str__(self):
        out = ""
        for i in range(len(self.board)):
            if i % 6 == 0:
                out += "| "
            out += str(self.board[i]) + " "
        out += "|"
        return out