'''
dfs(i,j), where i is number of digits we build so far and j is the last digit in builded numbers
dfs(3,2) = [212, 432, 232]
leading zero: i == 1 and j == 0, except n == 1
corner case: k = 0, in which j == next_j

'''

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        
        @lru_cache(None)
        def dfs(i, cur_digit):
            if cur_digit < 0 or cur_digit > 9:
                return []
            if cur_digit == 0 and i == 1: # leading 0
                return []
            if i == 1:
                return [str(cur_digit)]
            res = []
            dirs = set([k, -k])
            for d in dirs:
                left_digit = cur_digit + d
                for path in dfs(i-1, left_digit):
                    res.append(path + str(cur_digit))
            return res
        
        ans = []
        for num in range(10):
            ans += dfs(n, num)
        return ans