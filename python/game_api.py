__author__ = 'Anthony'

from board import Board
from minimax import MinimaxTree

class GameApi():
    def play(self, board):
        self.board = Board(self.parse_board(board))
        if self.board.evaluate('O') == 'O' or len(self.board.availables_moves()) == 0: return [], 'game_over'
        AI_player = MinimaxTree(self.board)
        cpu_move = AI_player.find_best_move()
        self.board.place('X', cpu_move)
        if self.board.evaluate('X') == 'X' or len(self.board.availables_moves()) == 0: return cpu_move, 'game_over'

        return cpu_move, 'playing'

    def parse_board(self, str_board):
        board = []
        rows = str_board.split('/')
        for i, r in enumerate(rows):
            colums = r.split(',')
            board.append([])
            for c in colums:
                board[i].append(c)

        return board        

if __name__ == "__main__":
    import sys
    api = GameApi()
    str_board = sys.argv[1]
    best_move, state = api.play(str_board)
    print(best_move)
    print(state)
    if state == 'game_over':
        winner_positions = api.board.winner_positions()
        print(winner_positions)
    sys.stdout.flush()