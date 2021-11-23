class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # O(mn)/O(1)
        m, n = len(mat), len(mat[0])
        r, c = 0, 0
        res = []
        for i in range(m * n):
            res.append(mat[r][c])
            if (r+c) % 2 == 0:
                # going up
                if c == n-1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                # going down
                if r == m-1:
                    c += 1
                elif c == 0:
                    r += 1    
                else:
                    r += 1
                    c -= 1
        return res
    
    
        # O(mn)/O(mn)
        d = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                d[i+j].append(mat[i][j])
        
        res = []
        for k in range(m+n-1):
            ls = d[k]
            if k % 2 == 0:
                res += ls[::-1]
            else:
                res += ls
        return res
        
        # TLE, O((m+n)^2)/O(1)
        m, n = len(mat), len(mat[0])
        res = []
        for s in range(0, m + n - 1):
            # i + j = s
            for i in range(s+1):
                j = s - i
                if s % 2 == 0: # left to right
                    i, j = j, i # swap to reverse, due to symmetirc
                if i >= m or j >= n:
                    continue
                res.append(mat[i][j])
        return res