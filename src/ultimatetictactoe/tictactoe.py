class TicTacToe():

    def __init__(self):
        self.active_player = 0
        self.is_won = False
        self.grid = [[None, None, None],
            [None, None, None],
            [None, None, None]]

    def switch_player(self):
        # 0 ~= X, 1 ~= O
        self.active_player = (self.active_player + 1) % 2

    def play(self, row, column, player=None):
        if self.grid[row][column] is None:
            if player is None:
                player = self.active_player
                self.switch_player()
            self.grid[row][column] = player
            return "X" if player == 0 else "O"
        else:
            return None
        
    def check_line(self, line):
        if all(map(lambda x: x == 0, line)):
            return 0
        elif all(map(lambda x: x == 1, line)):
            return 1
        else:
            return None
        
    def determine_victory(self):
        winner = None
        # horizontal
        for row in self.grid:
            winner = self.check_line(row)
            if winner is not None:
                return winner
        # vertical
        for i in range(3):
            column = [self.grid[row][i] for row in range(3)]
            winner = self.check_line(column)
            if winner is not None:
                return winner
            
        # diagonal
        diag1 = [self.grid[0][0], self.grid[1][1], self.grid[2][2]]
        diag2 = [self.grid[2][0], self.grid[1][1], self.grid[0][2]]

        for diag in (diag1, diag2):
            winner = self.check_line(diag)
            if winner is not None:
                return winner