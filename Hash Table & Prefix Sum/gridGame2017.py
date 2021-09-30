class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        '''
        grid: 2 x n
        (0, 0) => (1, n-1)
        '''
        # O(n)/O(n)
        n = len(grid[0])
        presum1, presum2 = [0], [0]
        for i in range(n):
            presum1.append(presum1[-1] + grid[0][i])
            presum2.append(presum2[-1] + grid[1][i])
        
        res = float('inf')
        for i in range(n):
            row1 = presum1[-1] - presum1[i+1]
            row2 = presum2[i]
            # print(row1, row2)
            p2 = max(row1, row2)
            res = min(res, p2)
        return res


class Solution2:
    def gridGame(self, grid: List[List[int]]) -> int:
        # O(n)/O(1)
        n = len(grid[0])
        ans = math.inf
        topSum = sum(grid[0])
        bottomSum = 0

        for i in range(n):
            topSum -= grid[0][i]
            ans = min(ans, max(topSum, bottomSum))
            bottomSum += grid[1][i]

        return ans