class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        dsu = DSU(26)
        char2idx = {c:i for i, c in enumerate(string.ascii_lowercase)}
        idx2char = {i:c for i, c in enumerate(string.ascii_lowercase)}

        for a, b in zip(A, B):
            a_id, b_id = char2idx[a], char2idx[b]
            if not dsu.isConnect(a_id, b_id):
                dsu.union(a_id, b_id)

        res = ""
        for s in S:
            cand = dsu.find(char2idx[s])
            res += idx2char[cand]
        return res
             
            
        
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr < yr: # smaller index as the parent
            self.p[yr] = xr
        else:
            self.p[xr] = yr

    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)