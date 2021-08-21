class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0 <= rowIndex <= 33
        @lru_cache(None)
        def dfs(row):
            if row == 0:
                return [1]
            ls = [0] + dfs(row - 1) + [0]
            res = []
            for a, b in zip(ls, ls[1:]):
                res.append(a + b)
            return res
        
        return dfs(rowIndex)