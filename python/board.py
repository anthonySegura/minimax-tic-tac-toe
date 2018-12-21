__author__ = 'Anthony'

import warnings
warnings.filterwarnings('ignore')

class Board():
    def __init__(self, board):
        self.board = board
        self.EMPTY = '-'

    def place_copy(self, player, position):
        board_copy = [row[:] for row in self.board]
        if board_copy[position[0]][position[1]] == self.EMPTY:
            board_copy[position[0]][position[1]] = player
        else:
            print('Invalid movement')
        return board_copy

    def place(self, player, position):
        if self.board[position[0]][position[1]] == self.EMPTY:
            self.board[position[0]][position[1]] = player
        else:
            raise Exception('Invalid movement')

    def availables_moves(self):
        positions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == self.EMPTY:
                    positions.append([i, j])
        return positions

    def evaluate(self, player):
        win_positions = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        if [player, player, player] in win_positions:
            return player

    def winner_positions(self):
        win_positions = [
            [[0,0], [0,1], [0,2]],
            [[2,0], [2,1], [2,2]],
            [[0,0], [1,0], [2,0]],
            [[0,1], [1,1], [2,1]],
            [[0,2], [1,2], [2,2]],
            [[0,0], [1,1], [2,2]],
            [[2,0], [1,1], [0,2]],
        ]
        for row in win_positions:
           moves = [self.board[p[0]][p[1]] for p in row] 
           if ['X', 'X', 'X'] == moves:
               return row
           elif ['O', 'O', 'O'] == moves:
               return row    

        return []       

    def __str__(self):
        str = ''
        for i in range(3):
            for j in range(3):
                str += self.board[i][j] + ' '
            str += '\n'
        return str            
        