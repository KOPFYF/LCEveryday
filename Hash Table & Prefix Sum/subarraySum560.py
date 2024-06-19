class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n)/O(n)
        res, presum, d = 0, 0, defaultdict(int)
        d[0] = 1
        for num in nums:
            presum += num
            res += d[presum - k]
            d[presum] += 1
        return res