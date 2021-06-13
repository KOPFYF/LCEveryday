class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        presum_row = [[0] * (n + 1) for _ in range(m)]
        presum_col = [[0] * n for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                presum_row[i][j+1] = presum_row[i][j] + grid[i][j]
                presum_col[i+1][j] = presum_col[i][j] + grid[i][j]
        # print(presum_row)
        # print(presum_col)
        
        res = 1
        for i in range(m):
            for j in range(n):
                diag = grid[i][j]
                for k in range(min(i, j)):
                    ii, jj = i-k-1, j-k-1
                    diag += grid[ii][jj]
                    ss = {diag} # for each block from (ii, jj) to (i,j), judge it!
                    for x in range(ii, i+1):
                        ss.add(presum_row[x][j+1] - presum_row[x][jj])
                    for y in range(jj, j+1):
                        ss.add(presum_col[i+1][y] - presum_col[ii][y])
                    ss.add(sum(grid[ii+kk][j-kk] for kk in range(k+2))) # anti-diagonal
                    if len(ss) == 1:
                        res = max(res, k+2)
        return res
                