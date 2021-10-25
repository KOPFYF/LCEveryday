class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1
        
        res = []
        while True:
            for j in range(l, r+1):
                res.append(matrix[u][j])   
            u += 1
            if u > d:
                break
            
            for i in range(u, d+1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            
            for j in range(r, l-1, -1):
                res.append(matrix[d][j]) 
            d -= 1
            if u > d:
                break
            
            for i in range(d, u-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        
        return res
                    