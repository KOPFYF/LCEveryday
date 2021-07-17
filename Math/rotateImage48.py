class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return
        def rotate(i, j):
            return j, n - 1 - i
        
        # (n + 1) // 2 total layers need, ex, n = 3, layer = 2
        # Layer i, its sideLength is (n-2*i)
        layer = (n + 1) // 2
        
        
        for i in range(layer): # from layer 0(out most) to layer-1
            for j in range(i, n - i - 1): # j ranges from i to n - i - 2, side len = n - 2*i
                
                ir, jr = rotate(i, j)
                ib, jb = rotate(ir, jr)
                il, jl = rotate(ib, jb)
                
                tmp = matrix[i][j]
                matrix[i][j] = matrix[il][jl]
                matrix[il][jl] = matrix[ib][jb]
                matrix[ib][jb] = matrix[ir][jr]
                matrix[ir][jr] = tmp