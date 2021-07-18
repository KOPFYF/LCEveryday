class Solution:
    def totalNQueens(self, n: int) -> int:
        # dig: x + y = p + q / x - y = p - q
        def dfs(i, col, diag, adiag):
            nonlocal res
            if i == n:
                res += 1
                return 
            for j in range(n):
                if j in col or i - j in diag or i + j in adiag:
                    continue
                col.add(j)
                diag.add(i - j)
                adiag.add(i + j)
                # path.append('.' * j + 'Q' + '.' * (n - j - 1))
                dfs(i + 1, col, diag, adiag)
                col.remove(j)
                diag.remove(i - j)
                adiag.remove(i + j)
                # path.pop()
        
        res = 0
        col, diag, adiag = set(), set(), set()
        dfs(0, col, diag, adiag)
        return res