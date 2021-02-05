class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # O(n^2) prefix sum
        # i, ..., j, ... k
        # a == b means a ^ b = 0 
        res = 0
        n = len(arr)
        for i in range(n):
            prefix = arr[i]
            for k in range(i + 1, n):
                prefix ^= arr[k]
                if prefix == 0:
                    res += (k - i)
        return res