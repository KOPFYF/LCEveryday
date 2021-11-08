class Solution(object):
    def isToeplitzMatrix(self, matrix):
        # return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
        #            for r, row in enumerate(matrix)
        #            for c, val in enumerate(row))
        
        # O(mn) / O(1)
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
    
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if i == 0 or j == 0:
                    continue
                if cell != matrix[i-1][j-1]:
                    return False
        return True