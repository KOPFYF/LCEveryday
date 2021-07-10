class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # O(n)/O(n)
        d = {0:-1}
        presum, res = 0, 0
        for i, num in enumerate(nums):
            # print(d)
            presum += num
            if presum not in d:
                d[presum] = i
            if presum - k in d:
                res = max(res, i - d[presum - k])
        return res