class Solution:
    def hammingWeight(self, n: int) -> int:
        # O(32)
        cnt = 0
        while n:
            n = n & (n - 1) # set rightmost 1 to 0
            cnt += 1
        return cnt