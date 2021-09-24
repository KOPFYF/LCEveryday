class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row, col, diag, adiag = [0] * 3, [0] * 3, 0, 0
        for i, (x, y) in enumerate(moves):
            if i % 2 == 0: # A
                row[x] += 1
                col[y] += 1
                if x == y:
                    diag += 1
                if x + y == 2:
                    adiag += 1
            else: # O
                row[x] -= 1
                col[y] -= 1
                if x == y:
                    diag -= 1
                if x + y == 2:
                    adiag -= 1
        res = row + col + [diag, adiag]
        # print(res)
        if 3 in res:
            return 'A'
        elif -3 in res:
            return 'B'
        elif len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'