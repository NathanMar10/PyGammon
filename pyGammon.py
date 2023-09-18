import numpy as np

class pyGammon:

    def __init__(self):
        self.board = np.zeros(24, dtype="int8")

    def __str__(self):
        out = ""
        for i in range(len(self.board)):
            if i % 6 == 0:
                out += "| "
            out += str(self.board[i]) + " "
        out += "|"
        return out