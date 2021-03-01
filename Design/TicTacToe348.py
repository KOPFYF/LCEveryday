class TicTacToe:
    '''
    Record the number of moves for each rows, columns, and two diagonals.
    For each move, we -1 for each player 1's move and +1 for player 2's move.
    Then we just need to check whether any of the recored numbers equal to n or -n.
    '''

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row, self.col = [0] * n, [0] * n
        self.diag, self.adiag, self.n = 0, 0, n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        offset = player * 2 - 3 # player 1; -1, player 2; +1
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.adiag += offset
        if self.n in (self.row[row], self.col[col], self.diag, self.adiag):
            return 2
        elif -self.n in (self.row[row], self.col[col], self.diag, self.adiag):
            return 1
        else:
            return 0
        
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)