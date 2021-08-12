'''
https://leetcode.com/problems/rank-transform-of-a-matrix/discuss/1391380/C%2B%2BPython-The-guy-who-is-downvoting-my-post-please-tell-me-why

process values from the smallest to largest, track the current rank for each row rows[i] and column col[j]

O(M*N * log(M*N)) / O(M*N)
'''
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        d = defaultdict(list)

        for r in range(m):
            for c in range(n):
                d[matrix[r][c]].append([r, c])

        rank = [0] * (m + n)  # rank[i] is the largest rank of the row or column so far.
        for a in sorted(d):
            uf = DSU()
            
            for r, c in d[a]:
                uf.union(r, c + m)  # Union row `r` with column `c` (column +m to separate with r)
            
            for group in uf.getGroups().values():
                maxRank = max(rank[i] for i in group)  # Get max rank of all included rows and columns
                for i in group: 
                    rank[i] = maxRank + 1  # Update all rows or columns in the same groups to new rank
            
            for r, c in d[a]:
                matrix[r][c] = rank[r]  # or matrix[r][c] = rank[c+m], both are correct!
            # print(matrix)

        return matrix

class DSU:
    def __init__(self):
        self.parent = {}
        
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        self.parent.setdefault(u, u)
        self.parent.setdefault(v, v)
        pu, pv = self.find(u), self.find(v)
        if pu != pv: 
            self.parent[pu] = pv
            
    def getGroups(self):
        groups = defaultdict(list)
        for i in self.parent.keys():
            groups[self.find(i)].append(i)
        return groups

