class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        res += 1
                    else:
                        tmp = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + matrix[i][j]
                        res += tmp
                        matrix[i][j] = tmp
        return res