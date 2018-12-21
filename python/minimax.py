__author__ = 'Anthony'


from board import Board

class MinimaxTree():
    def __init__(self, board, isMax=True, position=[], cpu_player='X'):
        self.current_board = board
        self.current_move = position
        self.isMax = isMax
        self.cpu_player = cpu_player
        self.best_move = None
        self.best_value = None
        self.nodes = []
        self.evaluate()

    def find_best_move(self):
        self.expand_node()
        return self.best_move

    def expand_node(self):
        # For terminal nodes
        if self.best_value != None:
            self.best_move = self.current_move
        else:
            positions = self.current_board.availables_moves()
            for p in positions:
                next_board = Board(self.current_board.place_copy('X' if self.isMax else 'O', p))
                next_game_node = MinimaxTree(next_board, isMax=(not self.isMax), position=p)
                next_game_node.expand_node()
                self.nodes.append(next_game_node)
                # Pruning
                if self.isMax and next_game_node.best_value == 1: break
                elif not self.isMax and next_game_node.best_value == -1: break

            if len(self.nodes) > 0:
                if self.isMax:
                    self.maximize()
                else:
                    self.minimize()
                self.nodes = None

    def evaluate(self):
        if self.current_board.evaluate(self.cpu_player):
            self.best_value = 1
        elif self.current_board.evaluate('O' if self.cpu_player == 'X' else 'X'):
            self.best_value = -1
        else:
            self.best_value = 0 if len(self.current_board.availables_moves()) == 0 else None

    def minimize(self):
        self.best_value, self.best_move = 2, []
        for n in self.nodes:
            if n.best_value < self.best_value:
                self.best_value = n.best_value
                self.best_move = n.current_move
                if self.best_value == -1:
                    break
        
    def maximize(self):
        self.best_value, self.best_move = -2, []
        for n in self.nodes:
            if n.best_value > self.best_value:
                self.best_value = n.best_value
                self.best_move = n.current_move
                if self.best_value == 1:
                    break
