class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # brute O(n^n), backtracking O(n!)/O(n)
        # There is N possibilities to put the first queen, not more than N (N - 2) to put the second one, not more than N(N - 2)(N - 4) for the third one etc. 
        # In total that results in \mathcal{O}(N!)O(N!) time complexity.
        # assume (x, y) is occupied, (p, q) where p + q == x + y or p - q == x - y would be invalid
        # slope = 1/-1, y = (-1)x + b -> y = -x + b -> y + x = b OR y = 1x + b -> y = x + b -> y - x = b
        res = []
        def dfs(path, i, col, diag, adiag):
            if i == n: 
                res.append(path)
                return
            for j in range(n):
                if j in col or (i - j) in diag or (i + j) in adiag:
                    continue
                col.add(j)
                diag.add(i - j)
                adiag.add(i + j)
                dfs(path + ["." * j + "Q" + "." * (n-j-1)], i+1, col, diag, adiag)
                col.remove(j)
                diag.remove(i - j)
                adiag.remove(i + j)
                
                # dfs(path + ["." * j + "Q" + "." * (n-j-1)], i+1, \
                #.    col | set([j]), diag | set([i-j]), adiag | set([i+j]))
                
        dfs([], 0, set(), set(), set())
        return res