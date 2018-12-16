__author__ = 'Anthony'

# TODO: - Implementar poda alpha-beta
#       - Interfaz gráfica con QT
#

from board import Board

class MinimaxTree():
    def __init__(self, board, state='MAX'):
        self.current_board = board
        self.current_move = []
        # Node state: min or max
        self.state = state
        self.cpu_player = 'X'
        self.state_value = None
        self.best_move = None
        self.best_state = None
        self.nodes = []
        self.evaluate()

    def evaluate(self):
        game_state = self.current_board.evaluate(['X', 'O'])
        # If the game is over
        if game_state != -1:
            # CPU Wins
            if game_state == self.cpu_player:
                self.state_value = 1
            # Tie
            elif game_state == 0:
                self.state_value = 0
            # CPU Loses
            elif game_state != self.cpu_player:
                self.state_value = -1

    def find_best_move(self):
        self.expand_node()
        return self.best_move

    def expand_node(self):
        # For terminal nodes
        if self.state_value != None:
            self.best_move = self.current_move
            self.best_state = self.state_value
            return

        positions = self.current_board.availables_moves()
        for p in positions:
            next_state = 'MIN' if self.state == 'MAX' else 'MAX'
            next_board = Board(self.current_board.place('O' if next_state == 'MAX' else 'X', p))
            next_game_node = MinimaxTree(next_board, next_state)
            next_game_node.current_move = p
            self.nodes.append(next_game_node)
            next_game_node.expand_node()

        if len(self.nodes) > 0:
            if self.state == 'MAX':
                self.maximize()
            else:
                self.minimize()
            self.nodes = None

    def minimize(self):
        val, mov = 2, []
        for n in self.nodes:
            if n.best_state < val:
                val = n.best_state
                mov = n.current_move
                if val == -1:
                    break
        self.best_state = val
        self.best_move = mov

    def maximize(self):
        val, mov = -2, []
        for n in self.nodes:
            if n.best_state > val:
                val = n.best_state
                mov = n.current_move
                if val == 1:
                    break
        self.best_state = val
        self.best_move = mov