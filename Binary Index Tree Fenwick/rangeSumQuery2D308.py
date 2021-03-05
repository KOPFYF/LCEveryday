class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.sums = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])     

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.sums[i][j] += delta
                j += self._lowbit(j)
            i += self._lowbit(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._query(row2, col2) + \
               self._query(row1 - 1, col1 - 1) - \
               self._query(row1 - 1, col2) - \
               self._query(row2, col1 - 1)
    
    def _query(self, row, col):
        s = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                s += self.sums[i][j]
                j -= self._lowbit(j)
            i -= self._lowbit(i)
        return s
                
    def _lowbit(self, x):
        return x & -x



class NumMatrix2:
    # Improve the initialization of BIT from above O(mnlogmlogn) to O(mn).
    def __init__(self, matrix):
        if not matrix: 
            return
        self.M, self.N = len(matrix), len(matrix[0])
        self.mat  = matrix
        self.BIT  = [[0] * (self.N + 1) for _ in range(self.M + 1)]
        # build BIT tree with Time O(mn) with dp in the following.
        for i in range(1, self.M + 1):
            temp = [0] * (self.N + 1)
            for j in range(1, self.N + 1):
                temp[j] += self.mat[i-1][j-1]
                if (j + (j & (-j))) <= self.N:
                    temp[j + (j & (-j))] += temp[j]
                self.BIT[i][j] += temp[j]
                if (i + (i & (-i))) <= self.M:
                    self.BIT[i + (i & (-i))][j] += self.BIT[i][j]

    def update(self, row, col, val):
        diff = val - self.mat[row][col]
        i, self.mat[row][col] = row + 1, val
        while i <= self.M:
            j = col + 1
            while j <= self.N:
                self.BIT[i][j] += diff
                j += (j & -j) 
            i += (i & -i)

    def sumRegion(self, row1, col1, row2, col2):
        return self.sumCorner(row2, col2) + self.sumCorner(row1 - 1, col1 - 1) - self.sumCorner(row1 - 1, col2) - self.sumCorner(row2, col1 - 1)

    def sumCorner(self, row, col):
        res, i = 0, row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.BIT[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res