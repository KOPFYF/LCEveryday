class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # O(n) 2 ptrs
        k = sum(data)
        n = len(data)
        tmp = sum(data[:k])
        res = k - tmp
        for i in range(n - k):
            tmp -= data[i]
            tmp += data[i + k]
            res = min(res, k - tmp)
        return res