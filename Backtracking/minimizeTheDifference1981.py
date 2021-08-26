class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        for row in mat:
            row.sort()
        min_sum = sum(row[0] for row in mat)
        max_sum = sum(row[-1] for row in mat)
        
        if target <= min_sum:
            return min_sum - target
        elif target >= max_sum:
            return target - max_sum
        
        nums = {0}
        for row in mat:
            nums = {x + i for x in row for i in nums}
        '''
        for row in mat:
            new_nums = set()
            for x in row:
                for val in nums:
                    new_nums.add(x+val)
            nums = new_nums
            '''
        return min(abs(target - x) for x in nums)



class Solution_Almost_TLE:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 1 <= m, n <= 70
        # backtracking + cache + pruning
        # O(mnt) = O(4900*800)
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            mat[i] = sorted(mat[i]) # remove duplicates
        
        
        @lru_cache(None)
        def dfs(i, cursum):
            if i == m:
                return abs(cursum - target)
            res = float('inf')
            for j in range(n):
                if j > 0 and mat[i][j] == mat[i][j - 1]: 
                    continue
                nxtsum = cursum + mat[i][j]
                res = min(res, dfs(i + 1, nxtsum))
                if nxtsum > target: # pruning 2, since it's sorted
                    break
            
            return res
        
        return dfs(0, 0)