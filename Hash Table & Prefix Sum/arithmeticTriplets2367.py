class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # O(n) / O(n)
        cnt = [0] * 201
        res = 0
        
        for num in nums:
            if num >= 2 * diff:
                res += int(cnt[num - diff] and cnt[num - 2*diff])
            cnt[num] = 1
        return res