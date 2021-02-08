class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def dfs(i, col, diag, adiag):
            if i == n: 
                self.res += 1
                return
            for j in range(n):
                if j in col or (i - j) in diag or (i + j) in adiag:
                    continue
                col.add(j)
                diag.add(i - j)
                adiag.add(i + j)
                dfs(i+1, col, diag, adiag)
                col.remove(j)
                diag.remove(i - j)
                adiag.remove(i + j)
                
                # dfs(i+1, col | set([j]), diag | set([i-j]), adiag | set([i+j]))
                
        dfs(0, set(), set(), set())
        return self.res
    
        # use code from 51
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
                
                # dfs(path + ["." * j + "Q" + "." * (n-j-1)], i+1, col | set([j]), diag | set([i-j]), adiag |set([i+j]))
                
        dfs([], 0, set(), set(), set())
        return len(res)