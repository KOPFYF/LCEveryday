class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # dig: x + y = p + q / x - y = p - q
        def dfs(path, i, col, diag, adiag):
            if i == n:
                res.append(path[:])
                return 
            for j in range(n):
                if j in col or i - j in diag or i + j in adiag:
                    continue
                col.add(j)
                diag.add(i - j)
                adiag.add(i + j)
                path.append('.' * j + 'Q' + '.' * (n - j - 1))
                dfs(path, i + 1, col, diag, adiag)
                col.remove(j)
                diag.remove(i - j)
                adiag.remove(i + j)
                path.pop()
        
        res = []
        col, diag, adiag = set(), set(), set()
        dfs([], 0, col, diag, adiag)
        return res
            