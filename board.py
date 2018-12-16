__author__ = 'Anthony'

import numpy as np
import warnings
warnings.filterwarnings('ignore')

class Board():
    def __init__(self, board):
        self.board = board
        self.EMPTY = '-'

    def place(self, player, position):
        board_copy = np.copy(self.board)
        if self.board[position[0], position[1]] == self.EMPTY:
            board_copy[position[0], position[1]] = player
        else:
            print('Invalid movement')
        return board_copy

    def play(self, player, position):
        if self.board[position[0], position[1]] == self.EMPTY:
            self.board[position[0], position[1]] = player
        else:
            raise Exception('Invalid movement')

    def availables_moves(self):
        return np.argwhere(self.board == self.EMPTY)

    def check_row_win(self, player):
        return np.any((np.all(self.board == player, axis=1)))

    def check_col_win(self, player):
        return np.any((np.all(self.board == player, axis=0)))

    def check_diag_win(self, player):
        diag1 = np.array([self.board[0, 0], self.board[1, 1], self.board[2, 2]])
        diag2 = np.array([self.board[0, 2], self.board[1, 1], self.board[2, 0]])
        return np.all(diag1 == player) or np.all(diag2 == player)

    def evaluate(self, players):
        winner = 0
        for player in players:
            if self.check_row_win(player):
                return player
            elif self.check_col_win(player):
                return player
            elif self.check_diag_win(player):
                winner = player
        if len(self.availables_moves()) == 0:
            winner = 0

        elif np.all(self.board != 0 and winner == 0):
            winner = -1
        return winner