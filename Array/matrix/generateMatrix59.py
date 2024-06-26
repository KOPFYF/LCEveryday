class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        u, d, l, r = 0, n - 1, 0, n - 1
        
        # res = list(range(1, n**2+1))
        idx = 1
        while True:
            for j in range(l, r+1):
                matrix[u][j] = idx
                idx += 1
            u += 1
            if u > d:
                break
            
            for i in range(u, d+1):
                matrix[i][r] = idx
                idx += 1
            r -= 1
            if l > r:
                break
            
            for j in range(r, l-1, -1):
                matrix[d][j] = idx
                idx += 1
            d -= 1
            if u > d:
                break
            
            for i in range(d, u-1, -1):
                matrix[i][l] = idx
                idx += 1
            l += 1
            if l > r:
                break
        
        return matrix