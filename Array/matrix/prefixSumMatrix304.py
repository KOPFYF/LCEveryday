class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix: return 
        m, n = len(matrix), len(matrix[0])
        self.M = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.M[i][j] = matrix[i - 1][j - 1] + self.M[i][j - 1] \
                            + self.M[i - 1][j] - self.M[i - 1][j - 1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.M[row2 + 1][col2 + 1] - self.M[row2 + 1][col1] \
             - self.M[row1][col2 + 1] + self.M[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)