'''
This a typical backtracking problem. Essentially, we have an array of 2*n-1 positions for which we progressively fill in numbers of 1, ..., n of which 1 has multiplicity 1 and the others have 2.

Here the strategy is that we aggresively fill in large numbers in high position if possible.
'''
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # 1 <= n <= 20
        # place the "large" number as front as possible.
        m = 2*n - 1
        res = [0] * m
        
        def dfs(i):
            if i == m: # base case loop to the end
                return True
            if res[i] and dfs(i + 1): # current i is filled, all after is True
                return True
            
            for j in range(n, 0, -1): # j from n to 1, greedy
                if j not in res:
                    step = j if j > 1 else 0
                    if i + step < m and res[i] == res[i + step] == 0: 
                        res[i] = res[i + step] = j # fill i/i+d with number j
                        if dfs(i + 1):
                            return True
                        res[i] = res[i + step] = 0 # backtracking
        
        dfs(0)
        return res