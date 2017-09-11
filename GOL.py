import numpy as np
import os
from time import sleep
from scipy import ndimage

def rule(n, orig):
    if n >= 4 or n <= 1:
        return 0
    elif n==3:
        return 1
    elif n==2:
        return orig
    else:
        return 0

class Board(object):
    """Board for the Game of Life"""
    def __init__(self, *args):
        super(Board, self).__init__()
        self.kernel = np.array([[1,1,1],
                                [1,0,1],
                                [1,1,1]])
        self.rule = np.vectorize(rule)
        if len(args) == 2:
            self.board = np.zeros((args[0], args[1]))
        elif len(args) == 1:
            self.board = np.zeros((args[0], args[0]))
        else:
            self.board = np.empty((0,0))



    def step(self):
        neighbors = ndimage.convolve(self.board, self.kernel, mode="wrap")
        self.board = self.rule(neighbors, self.board)

    def display(self, timeout):
        sleep(timeout)
        os.system('cls')
        for row in self.board:
            temp = ['.' if c==0 else '■' for c in row]
            print(''.join(temp))

    def draw(self, u, v):
        self.board[u, v] = 1-self.board[u, v]

if __name__ == '__main__':
    game = Board(10)
    game.display(0)
    game.draw(0,1)
    game.draw(1,2)
    game.draw(2,0)
    game.draw(2,1)
    game.draw(2,2)
    game.display(0.5)
    try:
        while True:
            game.step()
            game.display(0.1)
    except KeyboardInterrupt:
        pass