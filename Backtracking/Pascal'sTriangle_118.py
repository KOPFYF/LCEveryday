class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(numRows):
            ans.append(self.dfs(row))
        return ans
        
    @lru_cache(None)
    def dfs(self, row):
        if row == 0:
            return [1]
        ls = [0] + self.dfs(row - 1) + [0]
        res = []
        for a, b in zip(ls, ls[1:]):
            res.append(a + b)
        return res
