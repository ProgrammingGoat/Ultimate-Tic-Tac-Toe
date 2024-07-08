from .tictactoe import TicTacToe

class Game():
    # def __init__(self):
    #     self.active_player = 0
    #     self.main_game = TicTacToe()
    #     self.subgames = []
    #     self.next_move = (None, None)
    #     self.completed_squares = []
    #     for i in range(3):
    #          self.subgames.append([])
    #          for j in range(3):
    #               self.subgames[i].append(TicTacToe())

    def start(self):
        self.active_player = 0
        self.main_game = TicTacToe()
        self.subgames = []
        self.next_move = (None, None)
        self.completed_squares = []
        for i in range(3):
             self.subgames.append([])
             for j in range(3):
                  self.subgames[i].append(TicTacToe())

    def switch_player(self):
         self.active_player = (self.active_player + 1) % 2

    def play(self, i, j, k, l, player=None):
        # only allow legal moves
        # moves are always legal if the next move is a completed square
        if None not in self.next_move and (i, j) not in self.completed_squares and (i, j) != self.next_move:
            print("illegal move detected by game.py")
            return (None, None, None)
        
        if player is None:
            player = self.active_player
        placed = None
        subgame_win = None
        board_win = None

        placed = self.subgames[i][j].play(k, l, player)
        if placed is not None:
            self.switch_player()
            # next legal move is equivalent to current small move
            subgame_win = self.subgames[i][j].determine_victory()
            if subgame_win is not None:
                self.completed_squares.append((i, j))
                if subgame_win != -1:
                    self.main_game.play(i, j, player)
                board_win = self.main_game.determine_victory()
            self.next_move = (k, l) if (k, l) not in self.completed_squares else (None, None)
        return (placed, subgame_win, board_win)

# singleton instance
game = Game()