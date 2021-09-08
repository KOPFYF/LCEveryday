class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # O(ops)
        for x, y in ops:
            m = min(m, x)
            n = min(n, y)
        return m * n