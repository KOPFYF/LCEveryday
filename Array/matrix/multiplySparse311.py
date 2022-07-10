class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        '''
        m*n = m*k k*n
        use three vectors(array) to store the index and value of all non-zero elements
        '''
        # O(N) time and N here is the none-zero number.
        def dot_product(row, col):
            # O(m+n)
            i, j = 0, 0
            m, n = len(row), len(col)
            res = 0
            while i < m and j < n:
                idx_row, val_row = row[i]
                idx_col, val_col = col[j]
                if idx_row < idx_col:
                    i += 1
                elif idx_row > idx_col:
                    j += 1
                else:
                    res += val_row * val_col
                    i += 1
                    j += 1
            return res
        
        m, n, k = len(A), len(A[0]), len(B[0])
        row_vec = [[(j, A[i][j]) for j in range(n) if A[i][j] != 0] \
                   for i in range(m)] 
        col_vec = [[(i, B[i][j]) for i in range(n) if B[i][j] != 0] \
                   for j in range(k)]
        # print(row_vec)
        # print(col_vec)
        C = [[dot_product(row, col) for col in col_vec] for row in row_vec]
        
        return C
        
        
        
        
        # BRUTE FORCE, O(n^3)/O(1)
        m, p, n = len(mat1), len(mat1[0]), len(mat2[0])
        mat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for k in range(p):
                    mat[i][j] += mat1[i][k] * mat2[k][j]
        return mat