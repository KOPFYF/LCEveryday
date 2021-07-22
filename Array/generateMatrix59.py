class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        nums = list(range(1, n*n + 1))
        
        u, d, l, r, pos = 0, n - 1, 0, n - 1, 0
        while True:
            for j in range(l, r + 1):
                # print(res)
                res[u][j] = nums[pos]
                pos += 1
            u += 1
            if u > d: break
                
            for i in range(u, d + 1):
                # print(res)
                res[i][r] = nums[pos]
                pos += 1
            r -= 1
            if l > r: break
            
            for j in range(r, l - 1, -1):
                # print(res)
                res[d][j] = nums[pos]
                pos += 1
            d -= 1
            if u > d: break
                
            for i in range(d, u - 1, -1):
                # print(res)
                res[i][l] = nums[pos]
                
                pos += 1
            l += 1
            if l > r: break
        
        return res