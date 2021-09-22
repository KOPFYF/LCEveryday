'''
https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/discuss/1238730/Python-dp-O(mn*min(mn))-solution-explained

DP O(mn*min(m,n)) / O(mn)

Imagine, than we have original grid:

01 02 03 04 05
06 07 08 09 10
11 12 13 14 15
16 17 18 19 20

Then table dp(i, j, -1) will have values, which goes in direction (1, 1).

01 02 03 04 05
06 08 10 12 14
11 18 21 24 27
16 28 36 40 44

dp(i, j, 1) is used to hash another type of diagonals. It will look like this:

01 08 21 40 44
06 18 36 39 42
11 28 30 32 34
16 17 18 19 20

We will use lru_cache options here to get fast updates. 
Then we need to traverse all possible rhombus: 
we will have O(mn*min(m,n)) of them and carefully evaluate sum of elements on border: 
which can be separated into 4 sides, which I denoted p1, p2, p3, p4. 
Actually I do not like which indexes I have here, I think it can be improved (UPD, it is now)

'''

class Solution_dp:
    def getBiggestThree(self, grid):
        m, n, heap = len(grid), len(grid[0]), []
        
        def update(heap, num):
            # update the heap with new num
            if num not in heap:
                heapq.heappush(heap, num)
                if len(heap) > 3: 
                    heapq.heappop(heap)
            return heap
        
        for num in itertools.chain(*grid):
            # chain *: loop the num vertically 
            update(heap, num)
          
        @lru_cache(None)
        def dp(i, j, dr):
            if not 0 <= i < n or not 0 <= j < m: 
                return 0 # out of boundary
            return dp(i - 1, j + dr, dr) + grid[j][i]
        
        for q in range(1, (1 + min(m, n))//2):
            for i in range(q, n - q):
                for j in range(q, m - q):
                    p1 = dp(i + q, j, -1) - dp(i, j - q, -1)
                    p2 = dp(i - 1, j + q - 1, -1) - dp(i - q - 1, j - 1, -1)
                    p3 = dp(i, j - q, 1) - dp(i - q, j, 1)
                    p4 = dp(i + q - 1, j + 1, 1) - dp(i - 1, j + q + 1, 1)
                    update(heap, p1 + p2 + p3 + p4)

        return sorted(heap)[::-1]


class Solution_brute_force:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        '''
        1 <= m, n <= 50
        /\\ (runsum)
        \\/ (runsum2)
        '''
        # brute force
        res = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                runsum = grid[i][j]
                res.append(runsum)
                dist = 1
                while i + dist < m and j - dist >= 0 and j + dist < n:
                    ii, jl, jr = i + dist, j - dist, j + dist
                    runsum += grid[ii][jl] + grid[ii][jr]
                    runsum2 = 0
                    while True:
                        # shrink back
                        jl += 1
                        jr -= 1
                        ii += 1
                        if jl == n or jr == 0 or ii == m:
                            break # out of boundary
                        if jl == jr:
                            runsum2 += grid[ii][jl]
                            res.append(runsum + runsum2)
                            break
                        runsum2 += grid[ii][jl] + grid[ii][jr]
                    dist += 1
        res = list(set(res))
        res.sort(reverse=True)
        
        return res[:3]